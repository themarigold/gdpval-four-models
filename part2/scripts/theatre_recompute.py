"""Recompute theatre payroll (task 4520f882) three ways:
  R = rubric/expert method at expert rates (should reproduce the rubric numbers)
  E = rubric/expert method at CBA rates
  O = Opus's method (from its Payroll formulas) at CBA rates
Regulars play 5h rehearsal, 1h sound check, 8 perfs; the synth sub adds 2 audits and plays 1 perf.
"""

CBA = dict(base=251.06, guar=2008.50, reh=55.67, sc1=76.59)
EXP = dict(base=252.06, guar=2016.48, reh=56.67, sc1=77.59)

# (name, premium %, doubling %)
players = [
    ("violin", 0.20, 0.0),
    ("viola", 0.15, 0.0),
    ("cello", 0.15, 0.0),
    ("bass", 0.15, 0.25),
    ("guitarA", 0.15, 0.25),
    ("guitarB", 0.0, 0.25),
    ("trumpet", 0.20, 0.25),
    ("woodwind", 0.15, 0.45),
    ("horn", 0.15, 0.0),
]


def expert_method(r):
    """Expert workbook Roster formulas: Z=prem*(SC+reh+perf); AA=dbl*(SC+reh+perf+prem);
    AB=5.5%*(audit+SC+reh+perf+prem+dbl). Synth sub: perf=Base*shows, prem=0.5 (sub .25 + elec .25)."""
    out = {}
    reh = 5 * r["reh"]
    sc = r["sc1"]
    for n, p, d in players:
        perf = r["guar"]
        prem = (sc + reh + perf) * p
        dbl = (sc + reh + perf + prem) * d
        vac = 0.055 * (sc + reh + perf + prem + dbl)
        out[n] = dict(sc=sc, reh=reh, perf=perf, prem=prem, dbl=dbl, vac=vac,
                      total=sc + reh + perf + prem + dbl + vac)
    audit = 2 * r["base"]
    perf = r["base"] * 1
    prem = (sc + reh + perf) * 0.5
    vac = 0.055 * (audit + sc + reh + perf + prem)
    out["synth"] = dict(audit=audit, sc=sc, reh=reh, perf=perf, prem=prem, dbl=0.0, vac=vac,
                        total=audit + sc + reh + perf + prem + vac)
    return out


def opus_method(r):
    """Opus Payroll!I..U formulas (rounded to cents as Opus does).
    M = base for premium/doubling = perf + reh + SC (synth sub: shows*Base + reh + SC).
    Premium = M*prem%, Doubling = M*dbl% (not compounded), Vac = 5.5% of S."""
    out = {}
    rnd = lambda x: round(x + 1e-9, 2)
    reh = rnd(5 * r["reh"])
    sc = r["sc1"]
    for n, p, d in players:
        perf = rnd(max(r["guar"], 8 * r["base"]))
        M = perf + reh + sc
        prem = rnd(M * p)
        dbl = rnd(M * d)
        S = perf + reh + sc + prem + dbl
        vac = rnd(S * 0.055)
        out[n] = dict(sc=sc, reh=reh, perf=perf, prem=prem, dbl=dbl, vac=vac, total=S + vac)
    audit = rnd(2 * r["base"])
    perf = rnd(min(1.5 * r["base"] * 1, r["guar"]))
    M = rnd(1 * r["base"]) + reh + sc
    prem = rnd(M * 0.25)
    S = perf + reh + sc + audit + prem
    vac = rnd(S * 0.055)
    out["synth"] = dict(audit=audit, sc=sc, reh=reh, perf=perf, prem=prem, dbl=0.0, vac=vac, total=S + vac)
    return out


R = expert_method(EXP)
E = expert_method(CBA)
O = opus_method(CBA)

print(f"{'who':9} {'field':6} {'Rubric(exp rates)':>18} {'ExpMethod@CBA':>14} {'Opus@CBA':>10}  verdict")
for who in ["synth"] + [p[0] for p in players]:
    for f in ["audit", "sc", "reh", "perf", "prem", "dbl", "vac", "total"]:
        if f not in R[who]:
            continue
        a, b, c = R[who][f], E[who][f], O[who][f]
        if a == 0 and c == 0:
            continue
        same = abs(b - c) < 0.006
        print(f"{who:9} {f:6} {a:18.2f} {b:14.2f} {c:10.2f}  {'RATE-ONLY' if same else 'METHOD DIFFERS'}")
print("Opus grand total (gross incl. vac):", round(sum(v['total'] for v in O.values()), 2))
print("Opus vac total:", round(sum(v['vac'] for v in O.values()), 2))

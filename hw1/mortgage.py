"""
HW1 starter code
"""

from pathlib import Path


def amortize(apr, years, balance, monthly_pmt=None):
    """
    Projects an amortization schedule for a loan with monthly payments

    Parameters
    ----------
    apr : float
        The annual percentage rate on the loan
    years : int
        The term of the loan, in years
    balance : float
        The initial balance of the loan
    monthly_pmt : float, optional
        A specific monthly payment amount. If None is provided, the monthly
        payment amount should be solved to perfectly amortize the loan at the
        end of the term.

    Returns
    -------
        An object of type dict[str, list] containing the projected values.
    """
    # Your implementation
    
    schedule = {"Period":[], 
                "start_bal":[], 
                "interest":[],
                "bal_after_int":[], 
                "pmt":[], 
                "bal_after_pmt":[],
                "principal_repaid":[]}
    n = years *12
    i = apr/12
    if (monthly_pmt is None):
        v = 1 / (1 + i)
        ann = (1 - v**n) / i
        monthly_pmt = balance/ann
        
    start_bal = balance
    principal_repaid = 0
    for period in range(1, n+1):
        schedule["Period"].append(period)
        schedule["start_bal"].append(start_bal)
        
        interest = i*start_bal
        schedule["interest"].append(i*start_bal)
        
        schedule["bal_after_int"].append(start_bal + interest)
        
        pmt= min(monthly_pmt, schedule["bal_after_int"][period-1])
        if(period == n):
            pmt = schedule["bal_after_int"][period-1] # put remaining payment
        schedule["pmt"].append(pmt)
        
        bal_after_pmt = start_bal + interest - pmt
        schedule["bal_after_pmt"].append(bal_after_pmt)
        
        principal_repaid = start_bal - bal_after_pmt
        schedule["principal_repaid"].append(principal_repaid)
        start_bal = bal_after_pmt
        
        if schedule["bal_after_pmt"][period-1] <= 1e-10:
            continue
    return schedule
    


def write_csv(fname, amortization_schedule, round_precision=2):
    """
    Writes an amortization schedule to a file in CSV format. There's some
    assertions in here to help you check your amortization_schedule is valid.

    Parameters
    ----------
    fname : str
        The name of the file
    amortization_schedule
        An object returned by the `amortize` function
    round_precision : float, optional
        Number of decimals to round to, by default 2
    """

    file = Path(fname)
    folder = file.parent
    if not folder.exists():
        raise ValueError(f"Whoops, directory '{folder}' does not exist.")

    assert isinstance(amortization_schedule, dict), (
        "amortization_schedule is not a dictionary"
    )

    lengths = set()
    columns = amortization_schedule.values()
    assert len(columns) > 0, "Dictionary has no keys!"
    for col in columns:
        lengths.add(len(col))
    assert len(lengths) == 1, "Mismatch in length of lists in amortization_schedule"

    headers = list(amortization_schedule.keys())
    length = lengths.pop()
    with open(file, "w") as f:
        f.write(",".join(headers) + "\n")
        for i in range(length):
            record = []
            for header, col in zip(headers, columns):
                value = col[i]
                if header == "period":
                    if value == 0:
                        break
                    else:
                        record.append(str(value))
                else:
                    record.append(f"{value:0.{round_precision}f}")
            f.write(",".join(record) + "\n")


COMMISSION_PERCENTAGE = 0.0025
COMMISSION_VAT_PERCENTAGE = 0.12
PSE_CHARGE_PERCENTAGE = 0.00005
STAX_CHARGE_PERCENTAGE = 0.006
SCCP_CHARGE_PERCENTAGE = 0.0001

def calculate_charges(gross, is_sell=False):
    commission = gross * COMMISSION_PERCENTAGE
    commission_vat = commission * COMMISSION_VAT_PERCENTAGE
    pse_charge = gross * PSE_CHARGE_PERCENTAGE
    stax_charge = gross * STAX_CHARGE_PERCENTAGE if is_sell else 0
    sccp_charge = gross * SCCP_CHARGE_PERCENTAGE

    total = commission + commission_vat + pse_charge + stax_charge + sccp_charge

    return round(total, 2)
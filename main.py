from fastapi import FastAPI, Query
import httpx
from datetime import datetime, timedelta

app = FastAPI()

CURRENT_COOKIE = "mintproLeadId=; dealerUserName=682a7ae6b1efa20e7698849e; redirectionData=; permissions=LEAD_READ,TAB_CUSTOMER_READ,RECENT_LEADS_READ,TAB_EARNINGS_READ,TAB_LEAD_WRITE,CERTIFICATION_READ,CONTENTS_READ,CREATE_QUOTE,PROFILE_READ,HELP_CENTER,CUSTOMER_READ,TW_VERTICAL_READ,FW_VERTICAL_READ,MF_VERTICAL_READ,HEALTH_VERTICAL_READ,COMMERCIAL_VERTICAL_READ,HEALTH_ONE_PLAN,REFER_FRIENDS_CERTIFICATE,CERTIFICATION_CONTENT_VIEW,CV_QIS,HELP_CENTER_V2,EARNINGS_V2_READ,RENEWAL_REPORT,REWARDS,OFFERS,PARTNER_PUBLIC_PROFILE,LIFE_VERTICAL_READ,TERM_VERTICAL_READ,AP_GRID; customerId=; source=mint-pro; pospUserName=682a7ae6b1efa20e7698849e; category=partner; skippedRenewal=; permission=not_verified; leadId=; authToken=255b77e3962d182b4f0f4f4a718b9e19e5a9d489a3b5ec69ddb9a18160e4c39362df0483b5ce8bbb6520a492ff8c9fd5; tenant=turtlemint; rzp_unified_session_id=Sv8P3CC2Zyb9WI; adb=0; leadUtm=%7B%22utmSource%22%3A%22https%3A%2F%2Fapp.turtlemintpro.com%2F%22%2C%22utmMedium%22%3A%22referral%22%2C%22utmUrl%22%3A%22https%3A%2F%2Fpro.turtlemintinsurance.com%2Fv2%2Fcommercial-vehicle-insurance%2Fcreate%22%7D; _gcl_au=1.1.1482383165.1780047807; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2FNTqegzphWMVjDbHa8%2FEuzCldCNaJ3bg4%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B%2FM2q6Mm%2BJK%2BO52JaFpHoXIv6kjJgJwpA%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX188ajG%2FqCu%2BcccANxm9nd%2Bkjp2OiUW%2FxirT%2BUB4rG4BSbr5mFrnWlW2cba5%2FfZxwY5T4oOz4QTOVQ%3D%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2B0iN7FWoRrdDIzIxOlvcfgJCXKjeb%2BCknXAVxjpiNVLKDvg4ZexV1r; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX19ow0L%2FZ9L9rskknGa6sGBdnMOv9theYKf069H68HrEqWGBM0oTsBd4; rl_user_id=RudderEncrypt%3AU2FsdGVkX181Kfnar09oEBV4cE8wQqTbcPwfp9P0XHIgzvDH%2BeishURQd0idXKGZ; rl_trait=RudderEncrypt%3AU2FsdGVkX19X%2FShFaFbOmVBdu1iI9YRu59IP0jKCsZYMhUlIcvetiDgsROG3nRpw%2B3ctt0OXBMqIOpl96C0cZCzDfX0mJEiXMCxq8wQl9GG%2B%2B%2FwiT74fbybC2LW%2BSm42fkZYXboy%2FE3eVgoxs8WryAHU6GjXCWhHTR%2FY%2BAxfguI%3D; mp_94b72fe8fa0b0fbf2984f556ad073226_mixpanel=%7B%22distinct_id%22%3A%22682a7ae6b1efa20e7698849e%22%2C%22%24device_id%22%3A%2281c3cdbf-3a0f-44b4-99bb-de9f4bb57a74%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fapp.turtlemintpro.com%2F%22%2C%22%24initial_referring_domain%22%3A%22app.turtlemintpro.com%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%2C%22%24user_id%22%3A%22682a7ae6b1efa20e7698849e%22%7D; _fbp=fb.1.1780047807737.336916023357974960; ufi=1; PLAY_SESSION=ef6b1e3c1334edd1dde4d38544c82198696d10af-dealerUserName=682a7ae6b1efa20e7698849e&pospUserName=682a7ae6b1efa20e7698849e&tenant=turtlemint&agent_mobile=9356445713&host=http%3A%2F%2Fmotor-service%3A9000&X-Forwarded-For=49.15.84.22%2C+64.252.100.130%2C49.15.84.22&x-partner-id=682a7ae6b1efa20e7698849e&broker=turtlemint&dealerName=sarfraj+husen+shaikh&mobile=9356445713&x-flow-type=b2b; rl_session=RudderEncrypt%3AU2FsdGVkX18vBPVBvT6dWs4gI%2BrpCyPK5Uw30gFp%2Blkyjr4yhOFGBdgqmObol3ekMfDtq7TU6RsKMCBGqCBW0ywO%2F6Q%2Bpwoc%2F26TRHNWkIFWwxp8C9Q8eb0U2%2B9sFNr9z%2Bkl39h3nEh97PEQXBnvzw%3D%3D"

async def fetch_vehicle_data(reg_no: str, vertical: str, client: httpx.AsyncClient):
    url = f"[https://pro.turtlemintinsurance.com/api/fetchVehicleDetails?registrationNumber=](https://pro.turtlemintinsurance.com/api/fetchVehicleDetails?registrationNumber=){reg_no}&vertical={vertical}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'application/json, text/plain, */*',
        'Referer': '[https://pro.turtlemintinsurance.com/](https://pro.turtlemintinsurance.com/)',
        'Cookie': CURRENT_COOKIE
    }
    response = await client.get(url, headers=headers)
    return response.json()

@app.get("/api/rc")
async def get_rc_details(reg_no: str = Query(..., description="Vehicle Registration Number")):
    if not reg_no:
        return {"status": "error", "message": "Please provide registration number.", "data": None}
    
    reg_no = reg_no.upper().strip()
    
    async with httpx.AsyncClient(verify=False) as client:
        raw_data = await fetch_vehicle_data(reg_no, "TW", client)
        
        val_result = raw_data.get('validateRegistrationResult', {})
        if val_result.get('status') == 'Error':
            mismatch_fields = val_result.get('mismatchFields', [])
            if mismatch_fields:
                correct_vertical = mismatch_fields[0].get('rtoValue')
                raw_data = await fetch_vehicle_data(reg_no, correct_vertical, client)
        
        reg_data = raw_data.get('registrationResult')
        
        if not reg_data:
            return {"status": "error", "message": "No details found.", "data": None}
            
        if reg_data.get('status') == 'WARNING':
            return {"status": "error", "message": "Server warning. Cookie expired or details blocked.", "data": None}

        reg_date_str = reg_data.get('registrationDate', '')
        reg_date_fmt, validity_fmt = "NA", "NA"
        
        if reg_date_str:
            try:
                date_obj = datetime.strptime(reg_date_str.replace('/', '-'), '%d-%m-%Y')
                reg_date_fmt = date_obj.strftime('%d-%b-%Y')
                validity_obj = date_obj + timedelta(days=(15*365.25)-1)
                validity_fmt = validity_obj.strftime('%d-%b-%Y')
            except:
                pass

        vertical = reg_data.get('vertical', '')
        if vertical == 'TW': v_class = "M-Cycle/Scooter(2WN)"
        elif vertical == 'CV': v_class = "Commercial Vehicle"
        elif vertical == 'FW': v_class = "Light Motor Vehicle (LMV)"
        else: v_class = "NA"

        owner_name = f"{reg_data.get('ownerFirstName', '')} {reg_data.get('ownerLastName', '')}".strip()

        return {
            "status": "success",
            "message": " ",
            "data": {
                "Regn. No": reg_data.get('registrationNo', 'NA'),
                "Date of Regn.": reg_date_fmt,
                "Regn. Validity": validity_fmt,
                "Owner Serial": "1",
                "Chassis Number": reg_data.get('chasisno', 'NA'),
                "Engine / Motor Number": reg_data.get('engineno', 'NA'),
                "Owner Name": owner_name if owner_name else "NA",
                "Son / Daughter / Wife of": "NA",
                "Address": reg_data.get('permanentAddress', 'NA'),
                "Fuel": str(reg_data.get('fuel', 'NA')).upper(),
                "Emission Norms": "NA",
                "Vehicle Class": v_class,
                "Maker": reg_data.get('make', 'NA'),
                "Model": reg_data.get('model', 'NA'),
                "Color": "NA",
                "Body Type": reg_data.get('bodyType', 'NA'),
                "Seating Capacity": str(reg_data.get('seatingCapacity', 'NA')),
                "Unladen Weight": "NA",
                "Month - Year of Mfg.": reg_data.get('year', 'NA'),
                "Cubic Cap. (CC)": str(reg_data.get('cubicCapacity', 'NA')),
                "Wheel Base": "NA",
                "No of Cylinders": "NA",
                "Financier": reg_data.get('financierName') or "NA",
                "Registration Authority": f"{reg_data.get('rto', {}).get('lntLoc', '')} {reg_data.get('reg1', '')}".strip() or "NA"
            }
        }

@app.get("/")
def home():
    return {"message": " API is Live!"}

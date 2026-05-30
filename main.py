from fastapi import FastAPI, Query
import httpx
from datetime import datetime, timedelta

app = FastAPI()

# Aapki Cookie
CURRENT_COOKIE = "mintproLeadId=; dealerUserName=682a7ae6b1efa20e7698849e; redirectionData=; permissions=LEAD_READ,TAB_CUSTOMER_READ,RECENT_LEADS_READ,TAB_EARNINGS_READ,TAB_LEAD_WRITE,CERTIFICATION_READ,CONTENTS_READ,CREATE_QUOTE,PROFILE_READ,HELP_CENTER,CUSTOMER_READ,TW_VERTICAL_READ,FW_VERTICAL_READ,MF_VERTICAL_READ,HEALTH_VERTICAL_READ,COMMERCIAL_VERTICAL_READ,HEALTH_ONE_PLAN,REFER_FRIENDS_CERTIFICATE,CERTIFICATION_CONTENT_VIEW,CV_QIS,HELP_CENTER_V2,EARNINGS_V2_READ,RENEWAL_REPORT,REWARDS,OFFERS,PARTNER_PUBLIC_PROFILE,LIFE_VERTICAL_READ,TERM_VERTICAL_READ,AP_GRID; customerId=; source=mint-pro; pospUserName=682a7ae6b1efa20e7698849e; category=partner; skippedRenewal=; permission=not_verified; leadId=; authToken=255b77e3962d182b4f0f4f4a718b9e19e5a9d489a3b5ec69ddb9a18160e4c39362df0483b5ce8bbb6520a492ff8c9fd5; tenant=turtlemint; rzp_unified_session_id=Sv8P3CC2Zyb9WI; adb=0; leadUtm=%7B%22utmSource%22%3A%22https%3A%2F%2Fapp.turtlemintpro.com%2F%22%2C%22utmMedium%22%3A%22referral%22%2C%22utmUrl%22%3A%22https%3A%2F%2Fpro.turtlemintinsurance.com%2Fv2%2Fcommercial-vehicle-insurance%2Fcreate%22%7D; _gcl_au=1.1.1482383165.1780047807; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2FNTqegzphWMVjDbHa8%2FEuzCldCNaJ3bg4%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B%2FM2q6Mm%2BJK%2BO52JaFpHoXIv6kjJgJwpA%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX188ajG%2FqCu%2BcccANxm9nd%2Bkjp2OiUW%2FxirT%2BUB4rG4BSbr5mFrnWlW2cba5%2FfZxwY5T4oOz4QTOVQ%3D%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2B0iN7FWoRrdDIzIxOlvcfgJCXKjeb%2BCknXAVxjpiNVLKDvg4ZexV1r; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX19ow0L%2FZ9L9rskknGa6sGBdnMOv9theYKf069H68HrEqWGBM0oTsBd4; rl_user_id=RudderEncrypt%3AU2FsdGVkX181Kfnar09oEBV4cE8wQqTbcPwfp9P0XHIgzvDH%2BeishURQd0idXKGZ; rl_trait=RudderEncrypt%3AU2FsdGVkX19X%2FShFaFbOmVBdu1iI9YRu59IP0jKCsZYMhUlIcvetiDgsROG3nRpw%2B3ctt0OXBMqIOpl96C0cZCzDfX0mJEiXMCxq8wQl9GG%2B%2B%2FwiT74fbybC2LW%2BSm42fkZYXboy%2FE3eVgoxs8WryAHU6GjXCWhHTR%2FY%2BAxfguI%3D; mp_94b72fe8fa0b0fbf2984f556ad073226_mixpanel=%7B%22distinct_id%22%3A%22682a7ae6b1efa20e7698849e%22%2C%22%24device_id%22%3A%2281c3cdbf-3a0f-44b4-99bb-de9f4bb57a74%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fapp.turtlemintpro.com%2F%22%2C%22%24initial_referring_domain%22%3A%22app.turtlemintpro.com%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%2C%22%24user_id%22%3A%22682a7ae6b1efa20e7698849e%22%7D; _fbp=fb.1.1780047807737.336916023357974960; ufi=1; PLAY_SESSION=ef6b1e3c1334edd1dde4d38544c82198696d10af-dealerUserName=682a7ae6b1efa20e7698849e&pospUserName=682a7ae6b1efa20e7698849e&tenant=turtlemint&agent_mobile=9356445713&host=http%3A%2F%2Fmotor-service%3A9000&X-Forwarded-For=49.15.84.22%2C+64.252.100.130%2C49.15.84.22&x-partner-id=682a7ae6b1efa20e7698849e&broker=turtlemint&dealerName=sarfraj+husen+shaikh&mobile=9356445713&x-flow-type=b2b; rl_session=RudderEncrypt%3AU2FsdGVkX18vBPVBvT6dWs4gI%2BrpCyPK5Uw30gFp%2Blkyjr4yhOFGBdgqmObol3ekMfDtq7TU6RsKMCBGqCBW0ywO%2F6Q%2Bpwoc%2F26TRHNWkIFWwxp8C9Q8eb0U2%2B9sFNr9z%2Bkl39h3nEh97PEQXBnvzw%3D%3D"

# Primary Source: Turtlemint API
async def fetch_vehicle_data(reg_no: str, vertical: str, client: httpx.AsyncClient):
    url = f"https://pro.turtlemintinsurance.com/api/fetchVehicleDetails?registrationNumber={reg_no}&vertical={vertical}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://pro.turtlemintinsurance.com/',
        'Cookie': CURRENT_COOKIE
    }
    try:
        response = await client.get(url, headers=headers, timeout=15.0)
        if "application/json" not in response.headers.get("content-type", ""):
            return {"internal_api_error": f"Server returned non-JSON. Status: {response.status_code}."}
        return response.json()
    except Exception as e:
        return {"internal_api_error": f"Failed to connect primary: {str(e)}"}

# Backup Source: Acko PHP API
async def fetch_backup_data(reg_no: str, client: httpx.AsyncClient):
    url = f"https://fast.panfree.us.cc/acko.php?vehicle_no={reg_no}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        response = await client.get(url, headers=headers, timeout=12.0)
        return response.json()
    except Exception as e:
        return {"status": False, "message": f"Backup API failed: {str(e)}"}

# Helper function to check masking
def is_masked(value: str) -> bool:
    if not value or value == "NA":
        return True
    return "*" in str(value)

@app.get("/api/rc")
async def get_rc_details(reg_no: str = Query(..., description="Vehicle Registration Number")):
    if not reg_no:
        return {"status": "error", "message": "Please provide registration number.", "data": None}
    
    reg_no = reg_no.upper().strip()
    
    async with httpx.AsyncClient(verify=False) as client:
        # Step 1: Call Primary Source (Turtlemint)
        raw_data = await fetch_vehicle_data(reg_no, "TW", client)
        
        if isinstance(raw_data, dict) and "internal_api_error" in raw_data:
            return {"status": "error", "message": raw_data["internal_api_error"], "data": None}
            
        val_result = raw_data.get('validateRegistrationResult', {})
        if val_result.get('status') == 'Error':
            mismatch_fields = val_result.get('mismatchFields', [])
            if mismatch_fields:
                correct_vertical = mismatch_fields[0].get('rtoValue')
                raw_data = await fetch_vehicle_data(reg_no, correct_vertical, client)
                
                if isinstance(raw_data, dict) and "internal_api_error" in raw_data:
                    return {"status": "error", "message": raw_data["internal_api_error"], "data": None}
        
        reg_data = raw_data.get('registrationResult')
        
        # Initialize default values from Primary API
        chassis_no = "NA"
        engine_no = "NA"
        owner_name = "NA"
        reg_date_fmt, validity_fmt = "NA", "NA"
        v_class, maker, model, fuel, address, financier, rto_auth = "NA", "NA", "NA", "NA", "NA", "NA", "NA"
        seating, cubic_cap, mfg_year, body_type = "NA", "NA", "NA", "NA"

        if reg_data and reg_data.get('status') != 'WARNING':
            chassis_no = reg_data.get('chasisno') or reg_data.get('chassisNumber') or reg_data.get('maskedChassisNumber') or "NA"
            engine_no = reg_data.get('engineno') or reg_data.get('engineNumber') or reg_data.get('maskedEngineNumber') or "NA"
            owner_name = f"{reg_data.get('ownerFirstName', '')} {reg_data.get('ownerLastName', '')}".strip() or "NA"
            
            reg_date_str = reg_data.get('registrationDate', '')
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
            
            fuel = str(reg_data.get('fuel', 'NA')).upper()
            maker = reg_data.get('make', 'NA')
            model = reg_data.get('model', 'NA')
            address = reg_data.get('permanentAddress', 'NA')
            body_type = reg_data.get('bodyType', 'NA')
            seating = str(reg_data.get('seatingCapacity', 'NA'))
            mfg_year = reg_data.get('year', 'NA')
            cubic_cap = str(reg_data.get('cubicCapacity', 'NA'))
            financier = reg_data.get('financierName') or "NA"
            rto_auth = f"{reg_data.get('rto', {}).get('lntLoc', '')} {reg_data.get('reg1', '')}".strip() or "NA"

        # Step 2: Check if Primary Data is Missing or Masked
        if not reg_data or reg_data.get('status') == 'WARNING' or is_masked(chassis_no) or is_masked(engine_no):
            
            # Trigger Backup API
            backup_raw = await fetch_backup_data(reg_no, client)
            
            if backup_raw.get("status") is True and "data" in backup_raw:
                b_data = backup_raw["data"]
                
                # Verify if Backup data is also masked
                b_chassis = b_data.get("chassis_number", "NA")
                b_engine = b_data.get("engine_number", "NA")
                
                if is_masked(b_chassis) or is_masked(b_engine):
                    return {"status": "error", "message": "Info not found (Data Masked on both sources).", "data": None}
                
                # If backup has fresh unmasked data, override the variables
                chassis_no = b_chassis
                engine_no = b_engine
                owner_name = b_data.get("owner_name", owner_name)
                fuel = str(b_data.get("fuel_type", fuel)).upper()
                model = b_data.get("vehicle_name", model)
                
                # Format Year/Month from Backup if primary date was missing
                if reg_date_fmt == "NA" and b_data.get("registration_year"):
                    b_year = b_data.get("registration_year")
                    b_month = b_data.get("registration_month", 1)
                    try:
                        date_obj = datetime(int(b_year), int(b_month), 1)
                        reg_date_fmt = date_obj.strftime('%b-%Y')
                        validity_fmt = f"Valid up to {int(b_year) + 15}"
                    except:
                        pass
                
                if rto_auth == "NA" and b_data.get("rto_code"):
                    rto_auth = b_data.get("rto_code")
                
                if v_class == "NA" and backup_raw.get("type"):
                    v_class = backup_raw.get("type")
            else:
                # If primary was masked and backup completely failed or returned no data
                return {"status": "error", "message": "Info not found.", "data": None}

        # Step 3: Final Response Object Construction
        return {
            "status": "success",
            "message": " ",
            "data": {
                "Regn. No": reg_no,
                "Date of Regn.": reg_date_fmt,
                "Regn. Validity": validity_fmt,
                "Owner Serial": "1",
                "Chassis Number": chassis_no,
                "Engine / Motor Number": engine_no,
                "Owner Name": owner_name,
                "Son / Daughter / Wife of": "NA",
                "Address": address,
                "Fuel": fuel,
                "Emission Norms": "NA",
                "Vehicle Class": v_class,
                "Maker": maker,
                "Model": model,
                "Color": "NA",
                "Body Type": body_type,
                "Seating Capacity": seating,
                "Unladen Weight": "NA",
                "Month - Year of Mfg.": mfg_year,
                "Cubic Cap. (CC)": cubic_cap,
                "Wheel Base": "NA",
                "No of Cylinders": "NA",
                "Financier": financier,
                "Registration Authority": rto_auth
            }
        }

@app.get("/")
def home():
    return {"message": " API is Live!"}

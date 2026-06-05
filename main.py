from fastapi import FastAPI, Query
import httpx
from datetime import datetime, timedelta

app = FastAPI()

# Aapki Cookie
CURRENT_COOKIE = "_fbp=fb.1.1780629521262.473540389999173656; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FPB7nnzg7shfHKR%2FMgSELFm%2BieYeDDRFETsnMiY93XAGR1oftkljcorOwM2Eb9H%2F0e8rUIJJH4hA%3D%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19sZ%2BCTrYsxjVrn0UDOQu6ElmrKmaTa9ljs2KGnnwr8gy%2FFeFAEZSPN; _ga=GA1.1.1122713705.1780629527; _gcl_au=1.1.1832188315.1780629518.10755563.1780629558.1780629567; mp_somethingrandomstring_mixpanel=%7B%22distinct_id%22%3A%22%24device%3A0c348f1d-e190-46e0-ae1e-0e714d843ae0%22%2C%22%24device_id%22%3A%220c348f1d-e190-46e0-ae1e-0e714d843ae0%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fwww.turtlemintinsurance.com%2F%22%2C%22%24initial_referring_domain%22%3A%22www.turtlemintinsurance.com%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%22%24initial_referrer%22%3A%22https%3A%2F%2Fwww.turtlemintinsurance.com%2F%22%2C%22%24initial_referring_domain%22%3A%22www.turtlemintinsurance.com%22%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%7D; mp_178f2efb5698c708c4a5c0c7c20c7a40_mixpanel=%7B%22distinct_id%22%3A%22%24device%3A3ca8c599-2f2f-4d44-8578-346f2c09539e%22%2C%22%24device_id%22%3A%223ca8c599-2f2f-4d44-8578-346f2c09539e%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fwww.turtlemintinsurance.com%2F%22%2C%22%24initial_referring_domain%22%3A%22www.turtlemintinsurance.com%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%22%24initial_referrer%22%3A%22https%3A%2F%2Fwww.turtlemintinsurance.com%2F%22%2C%22%24initial_referring_domain%22%3A%22www.turtlemintinsurance.com%22%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%7D; _ga_RKQFLJSGZQ=GS2.1.s1780629526$o1$g1$t1780629581$j5$l0$h0; mintproLeadId=; dealerUserName=682a7ae6b1efa20e7698849e; redirectionData=; permissions=LEAD_READ,TAB_CUSTOMER_READ,RECENT_LEADS_READ,TAB_EARNINGS_READ,TAB_LEAD_WRITE,CERTIFICATION_READ,CONTENTS_READ,CREATE_QUOTE,PROFILE_READ,HELP_CENTER,CUSTOMER_READ,TW_VERTICAL_READ,FW_VERTICAL_READ,MF_VERTICAL_READ,HEALTH_VERTICAL_READ,COMMERCIAL_VERTICAL_READ,HEALTH_ONE_PLAN,REFER_FRIENDS_CERTIFICATE,CERTIFICATION_CONTENT_VIEW,CV_QIS,HELP_CENTER_V2,EARNINGS_V2_READ,RENEWAL_REPORT,REWARDS,OFFERS,PARTNER_PUBLIC_PROFILE,LIFE_VERTICAL_READ,TERM_VERTICAL_READ,AP_GRID; customerId=; pospUserName=682a7ae6b1efa20e7698849e; authToken=a4f8b966fad1a5b32e38b4565b10a74f5db45c87b662f7ac591253fd670518564cb79f1c4a25fc01422a052d3ba36a51; category=partner; skippedRenewal=; permission=not_verified; leadId=; tenant=turtlemint; leadUtm=%7B%22utmSource%22%3A%22https%3A%2F%2Fapp.turtlemintpro.com%2F%22%2C%22utmMedium%22%3A%22referral%22%2C%22utmUrl%22%3A%22https%3A%2F%2Fpro.turtlemintinsurance.com%2Fcar-insurance%2Fcreate%22%7D; isUtmParamsChange=true; mp_94b72fe8fa0b0fbf2984f556ad073226_mixpanel=%7B%22distinct_id%22%3A%22682a7ae6b1efa20e7698849e%22%2C%22%24device_id%22%3A%22f69e7cb1-e160-4cee-a5fb-8c83790e045e%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fapp.turtlemintpro.com%2F%22%2C%22%24initial_referring_domain%22%3A%22app.turtlemintpro.com%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%2C%22%24user_id%22%3A%22682a7ae6b1efa20e7698849e%22%7D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2FJn27io%2FCvYQ5e5dCYBdfaMMesPZ3Z3Wc%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX19R25g%2BlVHM3ogmtAQv7SzDAcFwsLpBttU%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FLJyJrNKrEEPqshKu%2B0A%2BdmDd%2FOlZcCb5%2Fhtgr60tADkky47ga3q3r; rl_user_id=RudderEncrypt%3AU2FsdGVkX19gCXqulR25X0FSKWUDAjCBhgyrwztU4xvJpj6%2Fh%2FJvPyFedYUjpdtZ; rl_trait=RudderEncrypt%3AU2FsdGVkX19aCNLSTouT2BLXvlmWhIeAlTzFFMqHLvRFamFWeA3do7wKi%2B6FoNaq%2Bd609YmP2NUdrapM1F%2FoXskx9oDoqj7V1uV6fbkoLGu9%2BODxmGNMsOtcAmn0J2%2BeZQfZwI4Ll8Kswc2oOHXkcBoIZmrheGQF8Y5P7mt6r5c%3D; _ga_JE764HVG8Y=GS2.1.s1780629653$o1$g0$t1780629653$j60$l0$h0; PLAY_SESSION=74a2c1ce55832e7e8fee54ac810a99564cdc2e05-dealerUserName=682a7ae6b1efa20e7698849e&pospUserName=682a7ae6b1efa20e7698849e&tenant=turtlemint&agent_mobile=9356445713&host=http%3A%2F%2Fmotor-service%3A9000&X-Forwarded-For=49.15.92.169%2C+64.252.100.5%2C49.15.92.169&x-partner-id=682a7ae6b1efa20e7698849e&broker=turtlemint&dealerName=sarfraj+husen+shaikh&mobile=9356445713&x-flow-type=b2b; rl_session=RudderEncrypt%3AU2FsdGVkX19psr6ylOL71Qji84MmAA4c7nGgIAkUtN677s6RMSAomYVRqhvyIhlT6EOG1WFkMYUh%2Bcl3gh552AocIXrsWPXDo76pvFsPILguhNKU%2Buz%2BXE320AfwMjF%2BNXHuzxqj0bfJbMPiLLnjLg%3D%3D"

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

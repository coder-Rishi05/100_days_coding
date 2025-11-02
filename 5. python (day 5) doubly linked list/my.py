"""
kisi bhi class ke attribute ya function runtime pe change krne ko monkey patching kehta han.


"""

import time

class ExternalService:
    def fetch_data(self):
        print("Starting slow network call")
        time.sleep(5)
        return "Real Data From Server"
    
api_service=ExternalService()

"""End of external service code"""

def runOriginal_call():
    start_time= time.time()
    result=api_service.fetch_data()
    end_time = time.time()
    print("result", result)
    print("time taken : {}".format(end_time-start_time))

def mock_fetch_data():
    print("Mock-Bypassing networkcall")
    return "Mocked Data"
   

def run_patched_data():
    api_service.fetch_data=mock_fetch_data


    start_time= time.time()
    result=api_service.fetch_data()
    end_time = time.time()
    print("result", result)
    print("time taken : {}".format(end_time-start_time))


def run_fetch_call(self):
     print("Mock - Bypassing network call")
     return "Mocked Test Data"



if __name__=="__main__":
        runOriginal_call()




# print(time.gmtime())
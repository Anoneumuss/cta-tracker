def unpackArrivalResponse(response: dict) -> list:
    """
    Turns the arrivals response.json and returns a corresponding list of records to be inserted into the database.

    Args:
        response (dict): The raw input json returned by the arrival api. 

    Returns:
        list: a list of dicts, each of which are records that will be inserted into the database.
    """

    # 1. Check if there was any data that was returned:
    if not response:
        raise Exception('Empty response.json()')
    
    # 2. Check the error codes
    ctatt = response['ctatt']
    tmst = ctatt['tmst']
    errCd = int(ctatt['errCd'])
    errNm = ctatt['errNm']

    if errCd or errNm:
        raise Exception(f"Error Code {errCd}: {errNm}")
    
    # 3. Return the data
    return ctatt['eta']
    




    

    

alert_failure_count = 0
threshold_value=180

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    if(celcius <= float(threshold_value)):
        return 200   # Return 200 for ok
    else:
        return 500   #Return 500 for not ok
    
def convert_farenheit_to_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    return celcius

def alert_in_celcius(farenheit):
    celcius = convert_farenheit_to_celcius(farenheit)
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1


alert_in_celcius(400.5)
alert_in_celcius(303.6)
print(f'{alert_failure_count} alerts failed.')
assert(alert_failure_count==1)
print('All is well (maybe!)')

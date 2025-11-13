





def adjust_thermostat(current_temp,targrt_temp):
    Fehrenheit_value=(targrt_temp*1.8)+32
    result=abs(current_temp-Fehrenheit_value)
    if current_temp<targrt_temp:
        return f"Hold {round(result,1) if result>=1 else round(result)} degree fehrenheit."
    elif current_temp>targrt_temp:
        return f"Cool {round(result,1) if result>0 else round(result)} degree fehrenheit."
    else:
        return "Hold."
 


print(adjust_thermostat(32,0))
print(adjust_thermostat(70,25))
print(adjust_thermostat(72,18))
# Understanding Static Methods 
# Static methods are those methods which does not depend on class or instance of class. 
# THese methods are independent but they are part of class.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# IN above class temperature conversion doesn't depend on class or instance its independent of class.
# Hence making them as staticmethod is good practice.
# Static methods can be accesed by classname or by instancename

tm1 = TemperatureConverter()
print(tm1.celsius_to_fahrenheit(30))
print(TemperatureConverter.celsius_to_fahrenheit(30))
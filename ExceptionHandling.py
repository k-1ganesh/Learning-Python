# Its done using try and except blocks.
# Critical part of code is kept in try block.
# If some exception occurs then except block is executed.


value = [5 ,4 ,2 , 0 , "Hi"]

for val in value:
    try:
        print(10 / int(val))
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print("I tried to divide")

# Finally is the block which is always excuted no matter whether exception raises or not.


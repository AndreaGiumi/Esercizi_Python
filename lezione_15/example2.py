with open("example2.txt", mode="w", encoding="utf-8") as file:
    message: str = "Hello, world!\n"
    written_char: int = file.write(message)
    print(f"Written characters: {written_char}")


    import time
    class StopWatch:
        def __init__(self):
            self.start_time = None
            self.end_time = None
# memorizza il tempo corrente
        def __enter__(self):

            self.start_time = time.time()

            return self
        
        def __exit__(self, exc_type, exc_value,traceback):
            self.end_time = time.time()
            elapsed_time = self.end_time - self.start_time
            print(f"elapsed time = {elapsed_time:-8f} seconds")

            if exc_type is not None:
                    print(f"Exception type = {exc_type}")
                    print(f"An error occurred = {exc_value}")
                    print(f"Traceback = {traceback}")

            return False
        
pass
    
with StopWatch():
    print("Hello, world!")
    time.sleep(2)
    print("Goodbye, world!")

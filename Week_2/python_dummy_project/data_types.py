# One-line examples of Python data types, each assigned to a variable.

# --- Numeric types ---
my_int = 42
my_float = 3.14
my_complex = 2 + 3j

# --- Text ---
my_str = "Hello, Python"

# --- Boolean ---
my_bool = True

# --- None (absence of a value) ---
my_none = None

# --- Sequence types ---
my_list = [1, 2, 3, "four", 5.0]          # ordered, mutable
my_tuple = (10, 20, 30)                   # ordered, immutable
my_range = range(5)                       # 0,1,2,3,4

# --- Set types ---
my_set = {1, 2, 3, 3, 2}                  # unique, unordered -> {1, 2, 3}
my_frozenset = frozenset([1, 2, 3])       # immutable set

# --- Mapping type ---
my_dict = {"name": "Asha", "age": 30}     # key -> value pairs

# --- Binary types ---
my_bytes = b"hello"                       # immutable bytes
my_bytearray = bytearray(b"hello")        # mutable bytes


if __name__ == "__main__":
    # Print each variable with its type
    for name, value in list(globals().items()):
        if name.startswith("my_"):
            print(f"{name:14} = {value!r:30} -> {type(value).__name__}")

from minir_datastructs.autogen.enum_string_description import BaseEnumStringDescription


class ValuePrimitiveKind(BaseEnumStringDescription):
    NONE =         ("none",          0, "No specific value type selected.")
    BOOL =         ("bool",          1, "Represents a boolean value type.")
    STRING =       ("string",        2, "Represents a string value type.")
    BYTES =        ("bytes",         5, "Represents a value type for a sequence of bytes.")
    BYTE =         ("byte",          9, "Represents a single byte value type.")
    INT =          ("int",          10, "Represents an integer value type.")
    FLOAT =        ("float",        11, "Represents a single-precision floating-point value type.")
    DOUBLE =       ("double",       12, "Represents a double-precision floating-point value type.")

class ValueSpecialKind(BaseEnumStringDescription): # Assuming BaseEnumWithStringSupport is defined
    NONE =       ("none",     0, "No specific type (or handled manually).")
    DIR =        ("dir",      1, "Path (writeable directory, creates if needed).")
    DIR_EXIST =  ("dire",     2, "Path (existing readable directory).")
    FILE =       ("file",     3, "Path (writeable file path).")
    FILE_EXIST = ("filee",    4, "Path (existing readable file).")
    PATH =       ("path",          5, "Path")

    DATE = ("date",    6, "")
    DATE_TIME = ("datet",    7, "")
    TIME = ("time",    8, "")
    UNIX = ("unix",    9, "")


class ValueDataType(BaseEnumStringDescription):
    PRIMITIVE           = ("primitive",           0,  "Represents basic primitive data types like int, byte, string, bool, etc.")
    CHILD_ARRAY         = ("child_array",         1,  "An array of a join entity where the current entity is the main object of the referenced join entity.")
    PARENT_ARRAY        = ("parent_array",        2,  "An array of a join entity where the current entity is a child object of the referenced join entity. Does not exist in *Data, *Struct, and *Records.")
    MAIN_OBJECT         = ("main_object",         3,  "The main object of a join entity. Does not exist in *Data, *Struct, and *Records.")
    CHILD_OBJECT        = ("child_object",        4,  "An object that is joined with the main object.")
    OBJECT              = ("object",              5,  "An object in a key entity representing a one-to-one relationship.")
    UNIQUE              = ("unique",              6,  "A unique string that will be used as a foreign key.")
    HASH                = ("hash",                7,  "A string that stores hashed values.")
    ENUM                = ("enum",                8,  "Read-only values where the ID represents a value of an enum.")
    DATE_TIME           = ("date_time",           9,  "Represents a date and time data type.")




class EntityType(BaseEnumStringDescription):
    NONE = ("none",  0, "Represents simple data struct that is never referenced anywhere and dont has any references or joins itself (exceptions are Inheretences, these are allowed).")
    KEY =  ("key", 1, "Represents a Key entity.")
    ENUM = ("enum", 2, "Represents an Enum entity.")
    JOIN = ("join", 5, "Represents a Join entity.")




class ClickParameterType(BaseEnumStringDescription):
    NONE =       ("none",     0, "No specific type (or handled manually).")
    DIR =        ("dir",      1, "Path (writeable directory, creates if needed).")
    DIR_EXIST =  ("dire",     2, "Path (existing readable directory).")
    FILE =       ("file",     3, "Path (writeable file path).")
    FILE_EXIST = ("filee",    4, "Path (existing readable file).")


class NameFormatting(BaseEnumStringDescription):
    NONE =     ("none",     0, "None.")
    CAMEL_CASE =     ("camel_case",     1, "Camel case.")
    UPPER_CAMEL_CASE =     ("upper_camel_case",     2, "Upper camel case.")
    PASCAL_CASE =     ("pascal_case",     3, "Pascal case.")
    SNAKE_CASE =     ("snake_case",     4, "Snake case.")
    UPPER_SNAKE_CASE =     ("upper_snake_case",     12, "Upper snake case.")
    ALL_UPPER_SNAKE_CASE =     ("all_upper_snake_case",     6, "All upper snake case.")
    KEBAB_CASE =     ("kebab_case",     5, "Kebab case.")
    UPPER_KEBAB_CASE =     ("upper_kebab_case",     13, "Upper kebab case.")
    ALL_UPPER_KEBAB_CASE =     ("all_upper_kebab_case",     7, "All upper kebab case.")
    LOWER_CASE =     ("lower_case",     8, "Lower case.")
    UPPER_CASE =     ("upper_case",     9, "Upper case.")
    REMOVE_SPECIAL =     ("remove_special",     10, "Remove special.")
    REMOVE_SPECIAL_AND_NUMBERS =     ("remove_special_and_numbers",     11, "Remove special and numbers.")
    VALID_CLASS =     ("valid_class",     14, "Valid class.")
    VALID_PARAMETER =     ("valid_parameter",     15, "Valid parameter.")


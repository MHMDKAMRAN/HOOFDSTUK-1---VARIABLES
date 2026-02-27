# Gemaakt door Kamran Mahmood,
# Vak: Scripting with Python, Hoofdstuk 3 - Variables
# Eigen oplossingen van de vijf oefeningen





# -----------------------
# Oefening 1 - Numbers
# -----------------------

my_100 = 100.00
my_50 = 50
my_25 = 25
print(type(my_100))
print(type(my_50))
print(type(my_25))
print(100.0+50.0+25.0)
print(my_50-my_25)


# -----------------------
# Oefening 2 - Boolean
# -----------------------



my_true = True
my_false = False
my_15 = 15
my_45 = 45
print(type(my_true))
print(type(my_false))
print(type(my_15))
print(type(my_45))
print(5 < 3)
print(5 < 10)
print(6 == 6)
print(6 == 3)
print(my_15 < my_45)
print(my_15 < 10)
print(my_45 == 45)
print(my_45 > my_15)




# -----------------------
# Oefening 3 - Strings
# -----------------------

student = " I am a student"

print(type(student))

print(student.index("a"))

print(student.count("a"))

print(student.find("stu"))

print(student.find("Stu"))

print(student.lower())

print(student.upper())

print(student.startswith(" "))

print(student.startswith("i"))

print(student.endswith("t"))

print(student.strip())

print(student.strip("t"))

print(len(student))

my_string = "Als een potvis in een pispot pist zit de pispot vol met potvispis."
print(my_string[-2])

my_string = "De koetsier poetst de postkoets met postkoetspoets."
print(my_string.count("o"))

my_string= "Als kakkerlakken in kattebakken kakken, heb je een kattebak vol met kakkerlakkak."
print(my_string.replace( " " , "_" ))

my_string_1 = "Knappe kappers kappen knap,"
my_string_2 = "maar de knecht van de knappe kapper kapt"
my_string_3 = "nog knapper dan de knappe kapper kappen kan."
print (my_string_1 + " " + my_string_2 + " " + my_string_3)





# -----------------------
# Oefening 4 - Lists
# -----------------------





my_combo = ["EHB", "Cisco", 2020, "switCHing"]
my_numbers = [100, 2020, 5, 103]

my_combo.append("router")
print(my_combo)

del my_combo[3]
print(my_combo)

my_combo.pop(0)
print(my_combo)

my_combo.remove("Cisco")
print(my_combo)

my_combo.insert(1, "Cisco")
print(my_combo)

my_vendor = ["Cisco", "Juniper", "Huawei", "HP"]
del my_vendor[3]
print(my_vendor)

my_vendor = ["Cisco", "Juniper", "Huawei", "HP"]
print(my_vendor[2])

my_vendor = ["Cisco", "Juniper", "Huawei", "HP"]
my_vendor.append("Ruckus")
print(my_vendor)

my_vendor = ["Cisco", "Juniper", "Huawei", "HP"]
print(my_vendor.index("Huawei"))

my_vendor = ["Cisco", "Juniper", "Huawei", "HP"]
my_vendor.insert(2, "Nokia")
print(my_vendor)

my_vendor = ["Cisco", "Juniper", "Huawei", "HP"]
my_vendor.sort()
print(my_vendor)

my_number = [100, 1000, 50, 53, 10, 123, 789]
print(min(my_number))
print(max(my_number))

my_vendor = ["Cisco", "Juniper", "Huawei", "HP"]
my_vendor_2 = ["Fortinet", "Arbor", "Aruba", "Checkpoint"]
my_vendor.extend(my_vendor_2)
print(my_vendor)


# --------------------------
# Oefening 5 - Dictionaries
# --------------------------



my_dict = {"Vendor":"Cisco", "Device":"3750", "Ports":"24", "IOS":"13"}

print(type(my_dict))
print(len(my_dict))
del my_dict["Ports"]
print(my_dict)
my_dict["RAM"] = 256
print(my_dict)
print("Vendor" in my_dict)
print("vendor" in my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict.pop('Device')
print(my_dict)
my_dict.update({"Speed" : "1Gb"})
print(my_dict)

scripting_languages = {1: "python", 2: "ruby", 3: "javascript", 4: "PHP", 5: "perl"}
ide_programs = {"ide_atom": "atom", "ide_vs": "visual_studio", "ide_pv": "py_dev", "ide_pc":
"pyCharm"}

print(type(scripting_languages))
print(type(ide_programs))

scripting_languages = {1: "python", 2: "ruby", 3: "javascript", 4: "PHP", 5: "perl"}
ide_programs = {"ide_atom": "atom", "ide_vs": "visual_studio", "ide_pv": "py_dev", "ide_pc":
"pyCharm"}

print("Scripting Language: " + scripting_languages[3])
print("IDE Program: " + ide_programs["ide_pv"])

scripting_languages = {1: "python", 2: "ruby", 3: "javascript", 4: "PHP", 5: "perl"}
ide_programs = {"ide_atom": "atom", "ide_vs": "visual_studio", "ide_pv": "py_dev", "ide_pc":
"pyCharm"}

print("Scripting Language: " + scripting_languages.get(1))
print("IDE Program: " + ide_programs.get("ide_pc"))

scripting_languages = {1: "python", 2: "ruby", 3: "javascript", 4: "PHP", 5: "perl"}


scripting_languages[4] = "bash"
print(scripting_languages)

ide_programs = {"ide_atom": "atom", "ide_vs": "visual_studio", "ide_pv": "py_dev", "ide_pc":
"pyCharm"}

ide_programs["ide_rm"] = "rubeMine"
print(ide_programs)

ide_programs = {"ide_atom": "atom", "ide_vs": "visual_studio", "ide_pv": "py_dev", "ide_pc":
"pyCharm"}

del ide_programs["ide_vs"]
print(ide_programs)

scripting_languages = {1: "python", 2: "ruby", 3: "javascript", 4: "PHP", 5: "perl"}

scripting_languages.pop(5)
print(scripting_languages)


scripting_languages = {1: "python", 2: "ruby", 3: "javascript", 4: "PHP", 5: "perl"}

scripting_values = scripting_languages.values()
print(scripting_values)
print(type(scripting_values))

list_scripting_values = list(scripting_values)
print(type(list_scripting_values))
print(list_scripting_values)

ide_programs = {"ide_atom": "atom", "ide_vs": "visual_studio", "ide_pv": "py_dev", "ide_pc": "pyCharm"}

program_keys = ide_programs.keys()
print(program_keys)
print(type(program_keys))

list_program_keys = list(program_keys)
print(list_program_keys)
print(type(list_program_keys))
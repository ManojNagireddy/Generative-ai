import os
import re
import faker


# **Schema Dictionary with Regex Patterns**
schema = {
    "first_name": {"faker": "first_name", "regex": r"^[A-Za-z ]+$"},
    "last_name": {"faker": "last_name", "regex": r"^[A-Za-z ]+$"},
    "address": {"faker": "address", "regex": r"^[A-Za-z0-9\s,.-]+$"},
    "HCID": {"generator": lambda: faker.Faker().numerify("##########"), "regex": r"^\d{9}$"},
    "UM_id": {"generator": lambda: faker.Faker().numerify("########"), "regex": r"^\d{8}$"},
    "DCN": {"generator": lambda: faker.Faker().numerify("##########"), "regex": r"^\d{9}$"},
    "policy number": {"generator": lambda: faker.Faker().numerify("######-####"), "regex": r"^\d{6}-\d{4}$"},
    "claim amount": {"generator": lambda: round(faker.Faker().random.uniform(100.0, 5000.0), 2), "regex": r"^\d+(\.\d{2})?$"},
    "ICD-10 codes": {"generator": lambda: faker.Faker().random_element(elements=("S06.0X0A", "I10", "Z91.81")), "regex": r"^[A-Z][0-9].[0-9]{1}([A-Z])?$"},
    "CPT codes": {"generator": lambda: faker.Faker().random_element(elements=("99213", "77067", "36415-59")), "regex": r"^\d{5}(?:-\d{1,2})?$"}
}


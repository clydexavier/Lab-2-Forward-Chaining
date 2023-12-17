import json
import re
import os
import time

"""FACTS SECTION"""
def input_facts(facts: list, fact: str):
    if fact in facts:
        return
    facts.append(fact)

# (list of facts, filename of json)
def save_facts(facts: list, filename: str):
    with open(filename, "w") as json_file:
        json.dump(facts, json_file)
        
def load_facts(mapping: dict, facts: list, filename: str):
    with open(filename, "r") as json_file:
        facts = json.load(json_file)
    return facts

"""RULES SECTION"""
def input_rules(mapping: dict, rules: list, complete_rules: list, rule: str):
    if rule not in complete_rules:
        complete_rules.append(rule)
    
    without_if = rule.split("if") #tanggal sa if
    without_then = without_if[1].split(", then") #tanggal sa then
    
    conditions = [condition.strip() for condition in without_then[0].split(" and")] #tanggal sa and
    action = without_then[1].strip() #consequent
    
    new_rule = (conditions, action) #tuple of antecedents and consequent
    
    if new_rule not  in rules:
        rules.append(new_rule)
       
def save_rules(rules: list, filename: str):
    with open(filename, "w") as json_file:
        json.dump(rules, json_file)

def load_rules(mapping: dict, rules: list, filename: str):
    with open(filename, "r") as json_file:
        rules = json.load(json_file)
    return rules

"""NEW FACTS"""
def generate_new_facts(mapping: dict, facts: list, rules: list):
    num_old_facts = len(facts)
    
    while len(rules) > 0:
        add = False
        for rule in rules:
            for r in rule[0]:
                ok = True
                if r not in facts:
                    ok = False
                    break
            if ok:
                add = True
                if rule[1] not in facts:
                    facts.append(rule[1])
                rules.remove(rule)
        if not add:
            break

    new_facts = facts[num_old_facts:]
    if len(new_facts) == 0:
        print("No new facts generated")
        return
    
    print(f"New facts generated: ")
    for f in new_facts:
        print(f)



def prompt():
    mapping = {}
    facts = []
    rules = []
    complete_rules = []
    facts = load_facts(mapping, facts, "facts.json")
    rules = load_rules(mapping, rules, "rules.json")
    complete_rules = load_rules(mapping, complete_rules, "complete_rules.json")
    os.system("cls")
    
    while True:
        print(f"Press number of choice...")
        user_input = input("1. Input Fact\n2. Input Rule\n3. Generate New Facts\n4. Display all facts\n5. Display all rules\n6. Save Facts\n7. Save Rules\n8. Reset Facts\n9. Reset Rules\n10. Exit\nYour choice: ")
        
        if user_input == "1":
            os.system("cls")
            fact = input("Enter new fact: ")
            input_facts(facts, fact)
            input("Press enter to continue...")
            os.system("cls")
        
        elif user_input == "2":
            os.system("cls")
            rule = input("Enter new rule: ")
            input_rules(mapping, rules, complete_rules, rule)
            input("Press enter to continue...")
            os.system("cls")
        
        elif user_input == "3":
            os.system("cls")
            generate_new_facts(mapping, facts, rules)
            input("Press enter to continue...")
            os.system("cls")
        
        elif user_input == "4":
            os.system("cls")
            print(f"All facts: ")
            for f in facts:
                print(f)
            input("Press enter to continue...")
            os.system("cls")
        
        elif user_input == "5":
            os.system("cls")
            print(f"All rules: ")
            for r in complete_rules:
                print(r)
            input("Press enter to continue...")
            os.system("cls")
        
        elif user_input == "6":
            os.system("cls")
            print(f"Saving Facts\n")
            input("Press enter to continue...")
            save_facts(facts, "facts.json")
            os.system("cls")

        elif user_input == "7":
            os.system("cls")
            print(f"Saving Rules\n")
            input("Press enter to continue...")
            save_rules(rules, "rules.json")
            save_rules(complete_rules, "complete_rules.json")
            os.system("cls")

        elif user_input == "8":
            os.system("cls")
            print(f"Resetting Facts\n")
            input("Press enter to continue...")
            facts.clear()
            save_facts(facts, "facts.json")
            os.system("cls")

        elif user_input == "9":
            os.system("cls")
            print(f"Resetting Rules\n")
            rules.clear()
            complete_rules.clear()
            save_rules(rules, "rules.json")
            save_rules(complete_rules, "complete_rules.json")
            input("Press enter to continue...")
            os.system("cls")
        
        elif user_input == "10":
            os.system("cls")
            exit()
        
        else:
            os.system("cls")
            print("Invalid Input")
            input("Press enter to continue...")
            os.system("cls")


class File:
    def __init__(self, name, facts, rules, complete_rules):
        self.name = name
        self.facts = facts
        self.rules = rules
        self.complete_rules = complete_rules

"""MAIN"""
if __name__ == "__main__":
    """os.system("cls")
    while True:
        print(f"Press number of choice...")
        user_input = input("1. Create new file\n2. Open an existing file\n3. Exit\n")
        
        if user_input == "1":
            os.system("cls")
        
        elif user_input == "2":
            os.system("cls")
        
        elif user_input == "3":
            os.system("cls")
            exit()"""
        
    prompt()
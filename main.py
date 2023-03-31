entities = {
    'provider': "natural or legal person, public authority, agency or other body that develops an AI system or that has an AI system developed and places that system on the market or puts it into service under its own name or trademark, whether for payment or free of charge",
    'user': "means any natural or legal person, including a public authority, agency or other body, under whose authority the system is used",
    'distributor': "any natural or legal person in the supply chain, other than the provider or the importer, that makes an AI system available on the Union market",
    'product manufacturer': "a manufacturer within the meaning of any of the Union harmonisation legislation listed in Annex II importer means any natural or legal person physically present or established in the Union that places on the market an AI system that bears the name or trademark of a natural or legal person established outside the Union",
    'authorised representative': "any natural or legal person physically present or established in the Union who has received and accepted a written mandate from a provider of an AI system to, respectively, perform and carry out on its behalf the obligations and procedures established by this Regulation",
    'operator': "the provider, the product manufacturer, the user, the authorised representative, the importer or the distributor"
}

# step one, are you any one of those entities?

def check_if_is_entity(entity):
    print("Are you any of the following entities?")
    # print the entities with a number in front of them
    for i, entity in enumerate(entities.keys()):
        print(f"{i + 1}. {entity}")

    is_entity = input("Enter the number of the entity you are, or enter 'none' if you are not any of the above: ")
    # get the entity name from the number
    return entities[list(entities.keys())[int(is_entity) - 1]] if is_entity != 'none' else None




activities = [
    "providers placing on the market or putting into service AI systems in the Union, irrespective of whether those providers are physically present or established within the Union or in a third country",
    "users of AI systems who are physically present or established within the Union",
    "providers and users of AI systems who are physically present or established in a third country, where the output produced by the system is used in the Union",
    "importers and distributors of AI systems",
    "product manufacturers placing on the market or putting into service an AI system together with their product and under their own name or trademark",
    "authorised representatives of providers, which are established in the Union"
]

# step two, what are you doing?
def what_are_you_doing():
    print("What are you doing?")
    for i, activity in enumerate(activities): # simplify this
        print(f"{i + 1}. {activity}")
    activity = input("Enter the number of the activity you are doing: ")
    return activities[int(activity) - 1] if activity != 'none' else None


systems = {
    'general purpose': "an AI system that - irrespective of how it is placed on the market or put into service, including as open source software - is intended by the provider to perform generally applicable functions such as image and speech recognition, audio and video generation, pattern detection, question answering, translation and others; a general purpose AI system may be used in a plurality of contexts and be integrated in a plurality of other AI systems",
    'AI system': "a system that is designed to operate with elements of autonomy and that, based on machine and/or human-provided data and inputs, infers how to achieve a given set of objectives using machine learning and/or logic- and knowledge based approaches, and produces system-generated outputs such as content (generative AI systems), predictions, recommendations or decisions, influencing the environments with which the AI system interacts"
}


# step three, is it a general purpose AI system?
def is_general_purpose():
    for i, system in enumerate(systems.keys()):
        print(f"{i + 1}. {system}")
    return input("Is it a general purpose AI system? (y/n): ") == 'y'

def is_personal():
    return input("Is it being used by natural persons only in purely personal or non-professional activities? (y/n): ") == 'y'

# secondary purposes
secondary_purposes = [
    "Public bodies in third countries using AI system within international framework for law enforcement and judicial co-operation",
    "Solely for scientific research",
    "AI R&D",
    "Military, Defense, National Security"
]
def is_secondary_purpose():
    print("Is it being used for any of the following secondary purposes?")
    for i, purpose in enumerate(secondary_purposes):
        print(f"{i + 1}. {purpose}")
    purpose = input("Enter the number of the purpose you are doing, or enter 'none' if you are not any of the above: ")
    return secondary_purposes[int(purpose) - 1] if purpose != 'none' else None


# Is the specific system already on or in service in the EU market?
def is_on_market():
    return input("Is the specific system already on or in service in the EU market? (y/n): ") == 'y'

# Is the system subject to significant change 12 months after teh EU AI act applies?
def is_significant_change():
    return input("Is the system subject to significant change 12 months after the EU AI act applies? (y/n): ") == 'y'


def EU_ACT_APPLIES():
    print("The EU AI act applies to you.")

def EU_ACT_DOES_NOT_APPLY():
    print("The EU AI act does not apply to you.")


def algorithm():
    # check if organization is an entity
    entity = check_if_is_entity(entities)
    if entity is None:
        EU_ACT_DOES_NOT_APPLY()
        return
    else:
        # check if organization is doing any of the activities
        activity = what_are_you_doing()
        if activity is None:
            EU_ACT_DOES_NOT_APPLY()
            return
        else:
            # which system is it?
            system = is_general_purpose()
            # is it being used by natural persons only in purely personal or non-professional activities?
            personal = is_personal()
            if personal:
                EU_ACT_DOES_NOT_APPLY()
                return
            else:
                # is it being used for any of the following secondary purposes?
                secondary_purpose = is_secondary_purpose()
                if secondary_purpose is None:
                    EU_ACT_DOES_NOT_APPLY()
                    return
                else:
                    # is the specific system already on or in service in the EU market?
                    on_market = is_on_market()
                    if on_market:
                        # changes?
                        significant_change = is_significant_change()
                        if significant_change:
                            EU_ACT_APPLIES()
                            return
                        else:
                            EU_ACT_DOES_NOT_APPLY()
                            return
                    else:
                        # applies to you
                        EU_ACT_APPLIES()
                        return

algorithm()

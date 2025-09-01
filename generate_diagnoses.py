import random
import json

def generate_diagnoses(num_diagnoses):
    diagnoses = []

    description_parts = {
        "opening": [
            "The patient exhibits a classic case of {disease_name}, a condition characterized by a profound sense of {symptom}.",
            "The subject's responses indicate a severe affliction of {disease_name}, which involves an obsessive longing for {longing}.",
            "We are seeing a textbook example of {disease_name}, where the patient is convinced that their missing {missing_item} have become quantumly entangled with a parallel universe.",
            "The inkblots reveal a case of {disease_name}, where the patient experiences a profound sense of anxiety and despair when faced with {context}.",
            "The subject appears to be suffering from {disease_name}, with a persistent and unshakeable belief that they are the main character in a grand, unfolding narrative."
        ],
        "manifestation": [
            "This may manifest as a deep-seated resentment towards {resentment} and a tendency to communicate in {communication}.",
            "This often leads to the belief that they were born in the wrong {wrong_era}, and they may be found frequenting {frequenting}.",
            "This leads to a compulsive need to purchase an excessive number of {purchased_item} in the hope that they will eventually stabilize their {stabilized_item}.",
            "This may result in a complete shutdown of the decision-making process, leading to the patient simply staring at {stared_at_item} until the establishment closes.",
            "This may manifest as a tendency to narrate their own life in the {narration_style}, and a deep-seated disappointment with their {supporting_cast}."
        ],
        "closing": [
            "The prognosis is uncertain, but we recommend a course of {treatment}.",
            "Further analysis is required, but we suspect a correlation with {correlation}.",
            "The patient's condition is exacerbated by their exposure to {exacerbated_by}.",
            "We believe this condition may be linked to a childhood trauma involving {childhood_trauma}.",
            "The only known cure is a strict regimen of {cure}."
        ]
    }

    disease_name_templates = [
        "{adjective} {noun} Syndrome",
        "Chronic {noun} Disorder",
        "Post-Traumatic {noun} Stress Disorder",
        "Quantum {adjective} {noun} Entanglement",
        "Existential {noun} Crisis",
        "Hyper-Ironic {noun} Detachment",
        "Benevolent {noun} Complex",
        "Aesthetic-Induced {noun}",
        "Cryptocurrency-Induced {noun} Mania",
        "Post-Structuralist {noun} Disorder",
        "Algorithmic {noun} Anxiety",
        "Competitive {noun} Empathy",
        "Semantic {noun} Satiation",
        "Irony-Deficiency {noun} Anemia",
        "Pre-Traumatic {noun} Stress Disorder",
    ]

    adjectives = ["Subterranean", "Recursive", "Quantum", "Existential", "Hyper-Ironic", "Benevolent", "Aesthetic-Induced", "Post-Structuralist", "Algorithmic", "Competitive", "Semantic", "Irony-Deficiency", "Pre-Traumatic", "Chronic", "Post-Traumatic"]
    nouns = ["Homesick Alienation", "Nostalgia", "Sock Drawer", "Buffet", "Protagonist", "Detachment", "Dictator", "Synesthesia", "Culinary", "Anxiety", "Empathy", "Satiation", "Anemia", "Stress"]
    symptoms = ["not belonging", "longing", "anxiety", "despair", "disappointment", "detachment", "bewilderment", "ennui"]
    longings = ["a past that never actually existed", "a future that will never be", "a sense of purpose", "a decent cup of coffee", "a reasonably priced avocado"]
    missing_items = ["socks", "keys", "motivation", "sense of self", "will to live"]
    contexts = ["an all-you-can-eat buffet", "an online dating app", "the cereal aisle", "a voting booth", "a choose-your-own-adventure novel"]
    resentments = ["popular culture", "the passage of time", "the laws of physics", "the concept of brunch", "the Oxford comma"]
    communications = ["a series of complex, indecipherable clicks and whistles", "interpretive dance", "memes and gifs", "vague and cryptic pronouncements", "passive-aggressive sighs"]
    wrong_eras = ["decade", "century", "millennium", "geological epoch", "timeline"]
    frequentings = ["vintage shops", "ren-faires", "internet forums dedicated to dead technologies", "the comments section of YouTube videos about classic rock", "their own imagination"]
    purchased_items = ["lottery tickets", "self-help books", "artisanal cheeses", "cryptocurrencies", "more socks"]
    stabilized_items = ["life", "quantum state", "emotional state", "financial portfolio", "sock drawer"]
    stared_at_items = ["food", "potential mates", "cereal boxes", "the ballot", "the page"]
    narration_styles = ["the third person", "the second person", "the first person plural", "an unreliable narrator", "the epistolary format"]
    supporting_casts = ["their supporting cast", "the people in their lives", "the general public", "their family", "their coworkers"]
    treatments = ["intensive meme therapy", "a strict social media detox", "a course of existential dread counseling", "a daily dose of reality television", "a trip to a remote, wifi-free location"]
    correlations = ["an overabundance of cat videos", "a deficiency in ironic detachment", "an excess of existential angst", "a latent desire to join the circus", "a subconscious belief in the healing power of crystals"]
    exacerbated_bys = ["late-stage capitalism", "the 24-hour news cycle", "the internet", "social media influencers", "the gig economy"]
    childhood_traumas = ["a particularly aggressive butterfly", "a traumatic experience with a mime", "a cheese-sculpting competition gone wrong", "a mermaid-themed birthday party", "a spontaneous disco fever outbreak"]
    cures = ["a steady diet of artisanal toast", "a pilgrimage to the birthplace of a forgotten 90s sitcom", "a vow of silence", "a complete and total rejection of modernity", "a subscription to a streaming service that only shows black and white films"]

    for _ in range(num_diagnoses):
        disease_name = random.choice(disease_name_templates).format(
            adjective=random.choice(adjectives),
            noun=random.choice(nouns)
        )

        opening = random.choice(description_parts["opening"])
        manifestation = random.choice(description_parts["manifestation"])
        closing = random.choice(description_parts["closing"])

        format_dict = {
            "disease_name": disease_name,
            "symptom": random.choice(symptoms),
            "longing": random.choice(longings),
            "missing_item": random.choice(missing_items),
            "context": random.choice(contexts),
            "resentment": random.choice(resentments),
            "communication": random.choice(communications),
            "wrong_era": random.choice(wrong_eras),
            "frequenting": random.choice(frequentings),
            "purchased_item": random.choice(purchased_items),
            "stabilized_item": random.choice(stabilized_items),
            "stared_at_item": random.choice(stared_at_items),
            "narration_style": random.choice(narration_styles),
            "supporting_cast": random.choice(supporting_casts),
            "treatment": random.choice(treatments),
            "correlation": random.choice(correlations),
            "exacerbated_by": random.choice(exacerbated_bys),
            "childhood_trauma": random.choice(childhood_traumas),
            "cure": random.choice(cures)
        }

        description = f"{opening.format(**format_dict)} {manifestation.format(**format_dict)} {closing.format(**format_dict)}"

        diagnoses.append({
            "name": disease_name,
            "description": description + " Also, you're probably gay."
        })

    return diagnoses

if __name__ == "__main__":
    diagnoses = generate_diagnoses(2000)
    with open("C:\\unlock-thyself\\services\\diagnoses.ts", "w", encoding="utf-8") as f:
        f.write("export const diagnoses = [\n")
        for diagnosis in diagnoses:
            f.write("  {\n")
            f.write(f"    name: {json.dumps(diagnosis['name'])},\n")
            f.write(f"    description: {json.dumps(diagnosis['description'])}\n")
            f.write("  },\n")
        f.write("];\n")

    print(f"Generated {len(diagnoses)} diagnoses and saved to C:\\unlock-thyself\\services\\diagnoses.ts")
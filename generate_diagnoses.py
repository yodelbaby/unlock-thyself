
import random
import json

def generate_diagnoses(num_diagnoses):
    diagnoses = []

    templates = [
        {
            "name": "{adjective} {noun} Syndrome",
            "description": "The patient exhibits a classic case of {name}, a condition characterized by a profound sense of {symptom}, often accompanied by the delusion that one is a {delusion}. This may manifest as a deep-seated resentment towards {resentment} and a tendency to communicate in a series of complex, indecipherable {communication}. The prognosis is uncertain, but we recommend a course of {treatment}."
        },
        {
            "name": "Chronic {noun} Disorder",
            "description": "The subject's responses indicate a severe affliction of {name}. This condition involves an obsessive longing for a {longing} that never actually existed, often leading to the belief that they were born in the wrong {wrong_era}. They may be found frequenting {frequenting}, speaking in outdated {outdated_slang}, and insisting that music was objectively better when it was recorded on {recording_medium}. Further analysis is required, but we suspect a correlation with {correlation}."
        },
        {
            "name": "Quantum {adjective} {noun} Entanglement",
            "description": "We are seeing a textbook example of {name}. The patient is convinced that their missing {missing_item} have not been lost, but have in fact become quantumly entangled with their counterparts in a parallel universe. This leads to a compulsive need to purchase an excessive number of {purchased_item}, in the hope that they will eventually stabilize the quantum state of their {stabilized_item}. The patient's condition is exacerbated by their exposure to {exacerbated_by}."
        },
        {
            "name": "Existential {noun} Crisis",
            "description": "The inkblots reveal a case of {name}. The patient experiences a profound sense of anxiety and despair when faced with an overwhelming number of choices, particularly in the context of a {context}. This may result in a complete shutdown of the decision-making process, leading to the patient simply staring at the {stared_at_item} until the establishment closes. We believe this condition may be linked to a childhood trauma involving {childhood_trauma}."
        },
        {
            "name": "Hyper-Ironic {noun} Detachment",
            "description": "The subject appears to be suffering from {name}. They have a persistent and unshakeable belief that they are the main character in a grand, unfolding narrative. This may manifest as a tendency to narrate their own life in the {narration_style}, an expectation of a dramatic plot twist at any moment, and a deep-seated disappointment with the {supporting_cast}. The only known cure is a strict regimen of {cure}."
        }
    ]

    adjectives = ["Subterranean", "Recursive", "Quantum", "Existential", "Hyper-Ironic", "Benevolent", "Aesthetic-Induced", "Post-Structuralist", "Algorithmic", "Competitive", "Semantic", "Irony-Deficiency", "Pre-Traumatic", "Chronic", "Post-Traumatic"]
    nouns = ["Homesick Alienation", "Nostalgia", "Sock Drawer", "Buffet", "Protagonist", "Detachment", "Dictator", "Synesthesia", "Culinary", "Anxiety", "Empathy", "Satiation", "Anemia", "Stress"]
    symptoms = ["not belonging", "longing", "anxiety", "despair", "disappointment", "detachment", "bewilderment", "ennui"]
    delusions = ["highly advanced extraterrestrial being", "time traveler", "sentient sock puppet", "figment of their own imagination", "character in a video game"]
    resentments = ["popular culture", "the passage of time", "the laws of physics", "the concept of brunch", "the Oxford comma"]
    communications = ["clicks and whistles", "interpretive dance", "memes and gifs", "vague and cryptic pronouncements", "passive-aggressive sighs"]
    longings = ["a past that never actually existed", "a future that will never be", "a sense of purpose", "a decent cup of coffee", "a reasonably priced avocado"]
    wrong_eras = ["decade", "century", "millennium", "geological epoch", "timeline"]
    frequentings = ["vintage shops", "ren-faires", "internet forums dedicated to dead technologies", "the comments section of YouTube videos about classic rock", "their own imagination"]
    outdated_slangs = ["slang", "jargon", "colloquialisms", "memes", "hashtags"]
    recording_mediums = ["wax cylinders", "8-track tapes", "floppy disks", "the blockchain", "oral tradition"]
    missing_items = ["socks", "keys", "motivation", "sense of self", "will to live"]
    purchased_items = ["socks", "lottery tickets", "self-help books", "artisanal cheeses", "cryptocurrencies"]
    stabilized_items = ["sock drawer", "life", "quantum state", "emotional state", "financial portfolio"]
    contexts = ["all-you-can-eat buffet", "online dating app", "the cereal aisle", "a voting booth", "a choose-your-own-adventure novel"]
    stared_at_items = ["food", "potential mates", "cereal boxes", "ballot", "the page"]
    narration_styles = ["third person", "second person", "first person plural", "unreliable narrator", "epistolary format"]
    supporting_casts = ["supporting cast", "people in their lives", "the general public", "their family", "their coworkers"]
    treatments = ["intensive meme therapy", "a strict social media detox", "a course of existential dread counseling", "a daily dose of reality television", "a trip to a remote, wifi-free location"]
    correlations = ["an overabundance of cat videos", "a deficiency in ironic detachment", "an excess of existential angst", "a latent desire to join the circus", "a subconscious belief in the healing power of crystals"]
    exacerbated_bys = ["late-stage capitalism", "the 24-hour news cycle", "the internet", "social media influencers", "the gig economy"]
    childhood_traumas = ["a particularly aggressive butterfly", "a traumatic experience with a mime", "a cheese-sculpting competition gone wrong", "a mermaid-themed birthday party", "a spontaneous disco fever outbreak"]
    cures = ["a steady diet of artisanal toast", "a pilgrimage to the birthplace of a forgotten 90s sitcom", "a vow of silence", "a complete and total rejection of modernity", "a subscription to a streaming service that only shows black and white films"]

    for _ in range(num_diagnoses):
        template = random.choice(templates)
        
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)

        name = template["name"].format(adjective=adjective, noun=noun)

        format_dict = {
            "name": name,
            "adjective": adjective,
            "noun": noun,
            "symptom": random.choice(symptoms),
            "delusion": random.choice(delusions),
            "resentment": random.choice(resentments),
            "communication": random.choice(communications),
            "longing": random.choice(longings),
            "wrong_era": random.choice(wrong_eras),
            "frequenting": random.choice(frequentings),
            "outdated_slang": random.choice(outdated_slangs),
            "recording_medium": random.choice(recording_mediums),
            "missing_item": random.choice(missing_items),
            "purchased_item": random.choice(purchased_items),
            "stabilized_item": random.choice(stabilized_items),
            "context": random.choice(contexts),
            "stared_at_item": random.choice(stared_at_items),
            "narration_style": random.choice(narration_styles),
            "supporting_cast": random.choice(supporting_casts),
            "treatment": random.choice(treatments),
            "correlation": random.choice(correlations),
            "exacerbated_by": random.choice(exacerbated_bys),
            "childhood_trauma": random.choice(childhood_traumas),
            "cure": random.choice(cures)
        }

        description = template["description"].format(**format_dict)

        diagnoses.append({
            "name": name,
            "description": description + " Also, you're probably gay."
        })

    return diagnoses

if __name__ == "__main__":
    diagnoses = generate_diagnoses(500)
    with open("C:\\unlock-thyself\\services\\diagnoses.ts", "w", encoding="utf-8") as f:
        f.write("export const diagnoses = [\n")
        for diagnosis in diagnoses:
            f.write("  {\n")
            f.write(f"    name: {json.dumps(diagnosis['name'])},\n")
            f.write(f"    description: {json.dumps(diagnosis['description'])}\n")
            f.write("  },\n")
        f.write("];\n")

    print(f"Generated {len(diagnoses)} diagnoses and saved to C:\\unlock-thyself\\services\\diagnoses.ts")

    print("\n--- Sample Diagnoses ---")
    for i in range(5):
        print(f"Name: {diagnoses[i]['name']}")
        print(f"Description: {diagnoses[i]['description']}\n")

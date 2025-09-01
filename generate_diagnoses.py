import random
import json

def generate_diagnoses(num_diagnoses):
    diagnoses = []

    templates = [
        {
            "name": "{adjective} {noun} Spectrum Disorder",
            "description": "The patient's profile suggests a presentation consistent with {name}, a condition characterized by a persistent sense of {symptom} and a pattern of {behavior}. This may manifest as a preoccupation with {preoccupation} and a tendency to engage in {coping_mechanism}. The recommended course of action is {treatment}."
        },
        {
            "name": "Latent {noun} Anxiety",
            "description": "The subject's responses are indicative of {name}. This condition involves a recurring preoccupation with {preoccupation}, often leading to a belief that they are deficient in {deficiency}. They may be found engaging in {behavior}, and insisting that {insistence}. Further analysis is required, but we suspect a correlation with {correlation}."
        },
        {
            "name": "Paradoxical {adjective} {noun} Response",
            "description": "We are observing a textbook example of {name}. The patient exhibits a paradoxical reaction to {stimulus}, resulting in a compulsive need to {compulsion}. This is often an attempt to stabilize their {stabilized_item}. The patient's condition is exacerbated by their exposure to {exacerbated_by}."
        },
        {
            "name": "Socio-Cognitive {noun} Dissonance",
            "description": "The inkblots reveal a case of {name}. The patient experiences a profound sense of cognitive dissonance when faced with {situation}, particularly in the context of {context}. This may result in a complete shutdown of the decision-making process, leading to the patient simply {coping_mechanism}. We believe this condition may be linked to a childhood trauma involving {childhood_trauma}."
        },
        {
            "name": "Normative {noun} Alienation",
            "description": "The subject appears to be suffering from {name}. They have a persistent and unshakeable belief that they are fundamentally different from their peers. This may manifest as a tendency to {behavior}, an expectation of {expectation}, and a deep-seated disappointment with {disappointment}. The only known cure is a strict regimen of {cure}."
        }
    ]

    adjectives = ["Affective", "Somatic", "Cognitive", "Behavioral", "Existential", "Ironic", "Normative", "Paradoxical", "Latent", "Chronic"]
    nouns = ["Dissonance", "Alienation", "Anxiety", "Nihilism", "Protagonist Syndrome", "Detachment", "Ambivalence", "Empathy Deficit", "Sonder", "Anhedonia"]
    symptoms = ["emotional dysregulation", "interpersonal difficulties", "a fragmented sense of self", "pervasive ennui", "a general sense of unease"]
    behaviors = ["maladaptive daydreaming", "excessive rumination", "social withdrawal", "intellectualization", "performative empathy"]
    preoccupations = ["the curated realities of social media", "the perceived inadequacies of their own life", "the futility of modern existence", "the search for authentic connection", "the aestheticization of everyday life"]
    coping_mechanisms = ["doomscrolling", "binge-watching nostalgic television shows", "engaging in ironic detachment", "curating a highly specific online persona", "listening to sad music in a minor key"]
    treatments = ["a course of radical acceptance", "a digital detox", "mindfulness-based stress reduction", "a semi-ironic return to traditional values", "a trip to a remote, wifi-free location"]
    deficiencies = ["cultural capital", "ironic detachment", "existential angst", "a coherent personal narrative", "a reasonable bedtime"]
    insistences = ["that their taste in music is objectively superior", "that they were born in the wrong generation", "that the book was better than the movie", "that they are 'not like other girls/boys'", "that they are 'an old soul'"]
    correlations = ["an overabundance of self-awareness", "a deficiency in serotonin", "an excess of student loan debt", "a latent desire to live in a cottage in the woods", "a subconscious belief in the transformative power of a new haircut"]
    stimulus = ["unsolicited advice", "performative optimism", "the pressure to be happy", "the commodification of self-care", "the relentless pace of modern life"]
    compulsions = ["purchase expensive candles", "reorganize their bookshelf by color", "start a podcast", "develop a niche hobby", "ironically adopt the mannerisms of a 1940s detective"]
    stabilized_items = ["their emotional state", "their sense of identity", "their online brand", "their carefully curated collection of houseplants", "their sourdough starter"]
    exacerbated_bys = ["late-stage capitalism", "the 24-hour news cycle", "the internet", "hustle culture", "the gig economy"]
    situations = ["an unstructured social gathering", "a networking event", "a group project", "a first date", "a family holiday"]
    contexts = ["a farm-to-table restaurant", "an artisanal coffee shop", "a co-working space", "a vintage clothing store", "a silent retreat"]
    expectations = ["a dramatic plot twist", "a cinematic meet-cute", "a moment of profound realization", "a spontaneous musical number", "a standing ovation"]
    disappointments = ["the supporting cast in their life", "the lack of a clear narrative arc", "the absence of a laugh track", "the mundanity of everyday life", "the quality of the catering"]
    childhood_traumas = ["being picked last for dodgeball", "a traumatic experience with a substitute teacher", "a poorly executed school play", "a family vacation to a theme park", "a dial-up internet connection"]
    cures = ["a steady diet of avocado toast", "a pilgrimage to the birthplace of a forgotten indie band", "a vow of digital silence", "a complete and total rejection of personal branding", "a subscription to a streaming service that only shows foreign films with subtitles"]

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
            "behavior": random.choice(behaviors),
            "preoccupation": random.choice(preoccupations),
            "coping_mechanism": random.choice(coping_mechanisms),
            "treatment": random.choice(treatments),
            "deficiency": random.choice(deficiencies),
            "insistence": random.choice(insistences),
            "correlation": random.choice(correlations),
            "stimulus": random.choice(stimulus),
            "compulsion": random.choice(compulsions),
            "stabilized_item": random.choice(stabilized_items),
            "exacerbated_by": random.choice(exacerbated_bys),
            "situation": random.choice(situations),
            "context": random.choice(contexts),
            "expectation": random.choice(expectations),
            "disappointment": random.choice(disappointments),
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
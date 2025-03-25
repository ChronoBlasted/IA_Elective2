import os
import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

tokenizer = AutoTokenizer.from_pretrained("dbddv01/gpt2-french-small")
model = AutoModelForCausalLM.from_pretrained("dbddv01/gpt2-french-small")

tokenizer.pad_token = tokenizer.eos_token  
model.config.pad_token_id = tokenizer.pad_token_id  

st.title("🎮 Générateur de Description")

max_length = st.slider("Longueur maximale de la description", 50, 300, 150)
temperature = st.slider("Créativité", 0.1, 1.5, 0.7)
num_beams = st.slider("Réflexion / Choix", 1, 10, 3)

st.write("Entrez une idée de jeu")
prompt_base = st.text_area("Décrivez brièvement votre jeu :", "Un jeu de rôle d'aventure dans un monde futuriste.")

if st.button("Générer"):
    with st.spinner("Génération en cours..."):

        prompt_desc = f"{prompt_base}"
        input_ids = tokenizer.encode(prompt_desc, return_tensors="pt")

        attention_mask = (input_ids != tokenizer.pad_token_id).type(input_ids.dtype)

        output_desc = model.generate(
            input_ids,
            attention_mask=attention_mask, 
            max_length=max_length,
            num_beams=num_beams,  
            temperature=temperature, 
            no_repeat_ngram_size=3,
            do_sample=True,
            top_k=50
        )

        description_generee = tokenizer.decode(output_desc[0], skip_special_tokens=True)

        st.subheader("📄 Description générée :")
        st.write(description_generee)

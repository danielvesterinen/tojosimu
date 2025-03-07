import random
import streamlit as st

# Lista kysymyksistä ja vastauksista (sisältää yhden kysymyksen esimerkkinä)
questions = [
    {
        "question": "Mikä on BOM?",
        "choices": ["Osaluettelo", "Toimittajan ylläpitämä varasto", "Varaston täydennysaika"],
        "answer": 0
    },
    {
        "question": "Mitä tarkoittaa VMI?",
        "choices": ["Varaston täydennysaika", "Osaluettelo", "Toimittajan ylläpitämä varasto"],
        "answer": 2
    },
    {
        "question": "Mikä seuraavista ei tarkoita samaa asiaa kuin varaston riitto?",
        "choices": ["Varaston riitto", "Varaston täydennysaika", "Varaston kierto"],
        "answer": 1
    },
    {
        "question": "Mihin tarvitaan INCOTERMS-lausekkeita?",
        "choices": ["Yksinkertaistamaan kauppasopimusten sisältöä", "Varastokustannusten hallintaan", "Kysynnän ennustamiseen"],
        "answer": 0
    },
    {
        "question": "Mitä tarkoittaa ATP?",
        "choices": ["Se osuus varastosta ja suunnitellusta tuotannosta, jota ei ole vielä kohdistettu millekään asiakkaalle", "Toimitusten hallinta", "Osaluettelo"],
        "answer": 0
    },
    {
        "question": "Mikä on kanban?",
        "choices": ["Kortti tai muu visuaalinen signaali, joka viestii tuotanto- ja täydennystarpeesta toimitusketjussa", "Varaston kiertonopeus", "Lean-työkalu"],
        "answer": 0
    },
    {
        "question": "Mitä tarkoittaa palvelutaso?",
        "choices": ["Varastotasojen hallinta", "Kysynnän ennustaminen", "Kuinka varasto tyydyttää kysynnän"],
        "answer": 2
    },
    {
        "question": "Kuinka lasketaan katekierto?",
        "choices": ["Myyntikate-% X Varaston kiertonopeus", "Myyntikate-% X Varaston riitto", "Myyntikate-% X Varaston kustannus"],
        "answer": 0
    },
    {
        "question": "Mitä ovat laadulliset kysyntäennustamismenetelmät?",
        "choices": ["Tilastolliset ennustemetodit", "Kvalitatiiviset menetelmät", "Asiantuntija-arvioihin perustuvat menetelmät"],
        "answer": 2
    },
    {
        "question": "Mikä seuraavista ei liity yhden kappaleen virtaukseen?",
        "choices": ["Tuotteet siirtyvät yksi kerrallaan", "Tuotteet siirtyvät erissä", "Tuotteet valmistetaan tilauksesta"],
        "answer": 1
    },
    {
        "question": "Mitkä seuraavista syistä aiheuttavat bullwhip-efektiä toimitusketjussa?",
        "choices": ["Hankintavaihtelut", "Asiakkaiden reagointi", "Puutetilanteisiin varautuminen ja ylitilaaminen", "Tuotteen varastointi", "Jatkuva tuotanto"],
        "answer": [0, 1, 2]
    },
    {
        "question": "Mitä lähtötietoja tarvitaan taloudellisen tilauseräkoon (EOQ) laskemiseen?",
        "choices": ["Varastonpitokustannukset", "Arvio tulevasta kysyntävolyymistä", "Tilauskustannukset", "Hankintahinta", "Toimituskulut"],
        "answer": [0, 1, 2, 3]
    },
    {
        "question": "Mitkä seuraavista asioista liittyvät imuohjaukseen?",
        "choices": ["Tuotteet valmistetaan vain välittömään kysyntään", "Tuotteet valmistetaan varastoon", "Varastojen täydennykset tehdään käytön perusteella", "Tuotteen jakelu"],
        "answer": [0, 2]
    },
    {
        "question": "Mitkä seuraavista ovat LEAN-tuotannon työkaluja?",
        "choices": ["Value stream mapping", "5S", "Kaizen", "Six Sigma", "Just-in-time"],
        "answer": [0, 1, 2]
    },
    {
        "question": "Mikä on asiakastilauksen kytkeytymispiste?",
        "choices": ["Toimitusketjun piste, jossa tapahtumat muuttuvat tilausohjautuviksi", "Toimitusketjun alku", "Toimitusketjun päätepiste"],
        "answer": 0
    },
    {
        "question": "Mikä on ABC-analyysi?",
        "choices": ["Asiantuntija-arvio", "Pareton periaate", "Tilastollinen menetelmä"],
        "answer": 1
    },
    {
        "question": "Mitä tarkoittaa 4PL?",
        "choices": ["Palveluntarjoaja, joka yhdistää eri logistiikkapalveluita", "Varaston optimointimenetelmä", "Toimitusketjun hallintatyökalu"],
        "answer": 0
    },
    {
        "question": "Mitä tarkoitetaan viivästyttämisellä?",
        "choices": ["Tuotteen loppukokoamisen viivyttäminen", "Tuotteen nopeuttaminen", "Tuotteen toimitusten viivästyminen"],
        "answer": 0
    },
    {
        "question": "Mikä on kiertovarasto?",
        "choices": ["Varasto, joka vaihtuu normaalin kulutuksen mukaan", "Varasto, joka ei vaihdu", "Varasto, joka vaihtelee tuotantotarpeiden mukaan"],
        "answer": 0
    },
    {
        "question": "Mikä on SKU?",
        "choices": ["Varastonimike", "Toimitusketjun hallintatyökalu", "Tilastollinen menetelmä"],
        "answer": 0
    },
    {
        "question": "Mitkä seuraavista ovat aikasarjamenetelmiä?",
        "choices": ["Eksponentiaalinen tasoitus", "Liukuva keskiarvo", "Keskiarvo", "Ennustaminen", "Analysointi"],
        "answer": [0, 1, 2]
    },
    {
        "question": "Mitä tarkoittaa varastonpitokustannuksiin luettava riskikustannus?",
        "choices": ["Mahdollisesta pilaantumisesta syntyvä kustannus", "Tilauksen tekemisestä syntyvä kustannus", "Kysynnän ennustamiseen liittyvä kustannus"],
        "answer": 0
    },
    {
        "question": "Kuinka lasketaan rahan sitoutumisaika?",
        "choices": ["Varastonkiertoaika + myyntisaamisten kiertoaika – ostovelkojen kiertoaika", "Myyntisaamisten kiertoaika + ostovelkojen kiertoaika – varastonkiertoaika", "Ostovelkojen kiertoaika + varastonkiertoaika – myyntisaamisten kiertoaika"],
        "answer": 0
    },
    {
        "question": "Mitä tarkoittaa kaupintavarasto?",
        "choices": ["Toimittajan omistama varasto asiakkaan toimipisteessä", "Asiakkaan omistama varasto toimittajan toimipisteessä", "Kolmannen osapuolen ylläpitämä varasto"],
        "answer": 0
    },
    {
        "question": "Mikä on 5S?",
        "choices": ["Menetelmä työpaikkojen organisointiin", "Kysynnän ennustamiseen liittyvä menetelmä", "Varastojen hallintamenetelmä"],
        "answer": 0
    },
    {
        "question": "Mikä on SMED?",
        "choices": ["Menetelmä asetusaikojen lyhentämiseen", "Menetelmä varastojen optimointiin", "Menetelmä toimitusketjun hallintaan"],
        "answer": 0
    },
    {
        "question": "Mitkä seuraavista ovat EOQ-kaavan lähtöoletuksia?",
        "choices": ["Tuleva kysyntä pystytään ennustamaan", "Varastoitavan tuotteen tarve on jatkuvaa", "Varastoitava tuote ei pilaannu tai vanhene", "Varastoitava tuote vanhenee nopeasti"],
        "answer": [0, 1, 2]
    },
    {
    "question": "Mitkä seuraavista lähtöoletuksista sisältyvät taloudellisen tilauseräkoon (EOQ) määrittämisen kaavaan?",
    "choices": ["Tuleva kysyntä pystytään ennustamaan", "Varastoitavan tuotteen tarve on jatkuvaa", "Varastoitava tuote ei pilaannu tai vanhene", "Varastoitava tuote pilaantuu nopeasti"],
    "answer": [0, 1, 2]
    },
    {
        "question": "Mitä tarkoittaa varastonpitokustannuksiin luettava riskikustannus?",
        "choices": ["Varastoitavan tavaran mahdollisesta pilaantumisesta tai arvonalenemisesta syntyvä kustannus", "Tilauskustannus", "Kuljetuskustannus"],
        "answer": 0
    },
    {
        "question": "Mikä on kiertovarasto?",
        "choices": ["Se osa varastosta, joka vaihtuu normaalin kulutuksen ja täydennysten rytmin mukaan", "Varastoitava tavara, joka ei koskaan vaihdu", "Varasto, jonka käyttö ei noudata mitään rytmiä"],
        "answer": 0
    },
    {
        "question": "Mikä on SKU?",
        "choices": ["Varastonimike", "Tilauskustannus", "Toimittajan ylläpitämä varasto"],
        "answer": 0
    },
    {
        "question": "Kuinka lasketaan rahan sitoutumisaika?",
        "choices": ["Varastonkiertoaika + myyntisaamisten kiertoaika – ostovelkojen kiertoaika", "Ostovelkojen kiertoaika + varastonkiertoaika – myyntisaamisten kiertoaika", "Myyntisaamisten kiertoaika + varastonkiertoaika – ostovelkojen kiertoaika"],
        "answer": 0
    },
    {
        "question": "Mitä tarkoittaa kaupintavarasto?",
        "choices": ["Toimittajan omistama ja ylläpitämä varasto asiakkaan toimipisteessä", "Asiakkaan omistama ja ylläpitämä varasto toimittajan toimipisteessä", "Kolmannen osapuolen ylläpitämä varasto"],
        "answer": 0
    },
    {
        "question": "Mitkä seuraavista asioista liittyvät imuohjaukseen?",
        "choices": ["Tuotteet valmistetaan vain välittömään kysyntään tai korvaamaan kysynnän mukaan toimitettuja tuotteita", "Pyritään minimoimaan varastoja", "Varastosta oton määrittää seuraava materiaaleja käyttävä vaihe", "Varastot täydennetään ennakoidun kysynnän perusteella"],
        "answer": [0, 1, 2]
    },
    {
        "question": "Mitkä seuraavista ovat LEAN-tuotannon työkaluja?",
        "choices": ["Value stream mapping", "5S", "Kaizen", "Six Sigma", "Just-in-time"],
        "answer": [0, 1, 2]
    },
    {
        "question": "Laskutehtävä a: Tarkastellaan yhtä varastoitavaa nimikettä. Nimikkeen vuotuinen kulutus on 2000 kpl, hankintahinta 1€/kpl, myyntihinta 3 €/kpl ja varaston keskimääräinen taso on 200 kpl. Varastonpitokustannusten laskennassa käytetään oppikirjoistakin tuttua arvoa 25%. Kuinka monta euroa ovat varastonpitokustannukset vuodessa?",
        "choices": ["50€", "100€", "200€"],
        "answer": 0
    },
    {
        "question": "Laskutehtävä b: Tarkastellaan tilannetta, jossa tiettyä nimikettä varastoidaan 9 eri varastossa. Varmuusvaraston koko kaikissa varastoissa on S, ja kaikissa on sama palvelutaso. Eri varastoihin kohdistuva kysyntä on toisistaan riippumatonta. Varastot keskitetään yhteen paikkaan. Kuinka suuri varmuusvarasto tässä uudessa tilanteessa tarvitaan, että pystytään pitämään sama palvelutaso kuin lähtötilanteessa? Oletetaan että täydennysaika ei muutu.",
        "choices": ["sqrt(9) = 3", "sqrt(9) = 2", "sqrt(9) = 4"],
        "answer": 0
    },
    {
        "question": "Laskutehtävä c: Tarkastellaan yhden nimikkeen varastonohjausta. Nimikkeen vuosikulutus on 1000 kpl, nimikkeen hankintahinta on 1 €/kpl, myyntihinta 3€/kpl, keskimääräinen täydennyserän koko on 40 kpl ja varmuusvarastotaso 10 kpl. Kuinka monta euroa tämä varasto keskimäärin sitoo pääomaa?",
        "choices": ["30€", "50€", "70€"],
        "answer": 0
    },
    {
        "question": "Laskutehtävä d: Tarkastellaan yhden nimikkeen varastonohjausta. Varaston ohjaukseen käytetään tilauspistejärjestelmää. Täydennyserän riitto on 14 päivää, täydennysviive on 3 päivää ja varmuusvarasto vastaa 4 päivän kysyntää. Millaiseksi muodostuu varaston riitto päivissä?",
        "choices": ["11 päivää", "14 päivää", "7 päivää"],
        "answer": 0
    }
]
def quiz():
    st.title("TOJO-Tenttiharjoittelu")
    st.write("Tervetuloa TOJO-Tenttiharjoitteluun!")

    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.questions_order = list(range(len(questions)))
        random.shuffle(st.session_state.questions_order)

    current_question_index = st.session_state.questions_order[st.session_state.current_question]
    score = st.session_state.score

    if st.session_state.current_question < len(questions):
        q = questions[current_question_index]
        st.write(f"Kysymys {st.session_state.current_question + 1}: {q['question']}")
        choices_selected = [st.checkbox(choice, key=f"{st.session_state.current_question}_{i}") for i, choice in enumerate(q["choices"])]
        user_answers = [i for i, selected in enumerate(choices_selected) if selected]

        if st.button("Vastaa", key=f"answer_button_{st.session_state.current_question}"):
            correct_answers = q["answer"]
            if isinstance(correct_answers, list):
                if sorted(user_answers) == sorted(correct_answers):
                    st.success("Oikein!")
                    score += 1
                else:
                    correct_answers_text = ', '.join([q["choices"][x] for x in correct_answers])
                    st.error(f"Väärin! Oikeat vastaukset ovat: {correct_answers_text}")
            else:
                if user_answers == [correct_answers]:
                    st.success("Oikein!")
                    score += 1
                else:
                    correct_answer_text = q["choices"][correct_answers]
                    st.error(f"Väärin! Oikea vastaus on: {correct_answer_text}")

            st.session_state.score = score
            st.session_state.current_question += 1

            if st.session_state.current_question < len(questions):
                st.experimental_set_query_params(rerun="true")
            else:
                st.write(f"Tentti päättyi. Sait oikein {score}/{len(questions)} kysymystä.")
                st.button("Aloita uudelleen", on_click=reset_quiz)

    else:
        st.write(f"Tentti päättyi. Sait oikein {score}/{len(questions)} kysymystä.")
        st.button("Aloita uudelleen", on_click=reset_quiz)

    if st.button("Lopeta tentti"):
        st.write(f"Tentti päättyi. Sait oikein {score}/{len(questions)} kysymystä.")
        st.button("Aloita uudelleen", on_click=reset_quiz)

def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.questions_order = list(range(len(questions)))
    random.shuffle(st.session_state.questions_order)
    st.experimental_set_query_params(reset="true")

if __name__ == "__main__":
    quiz()

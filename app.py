import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Agronomia Premium - Portal do Aluno",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        color: white;
        background-color: #2e7d32; /* Verde Agro */
        border-radius: 10px;
        width: 100%;
    }
    .stProgress > div > div > div > div {
        background-color: #2e7d32;
    }
    h1, h2, h3 {
        color: #1b5e20;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DADOS DO CURSO (BANCO DE DADOS SIMULADO) ---
# Aqui vamos adicionando as disciplinas conforme avançamos
course_data = {
    1: {
        "nome": "Empreendedorismo e Inovação",
        "status": "Disponível",
        "video_destaque": "https://www.youtube.com/watch?v=22-video-placeholder", # Simulação do ID Youtube
        "conteudo": """
        ### 🚀 A Dor é o seu Negócio
        
        **Resumo da Aula:**
        Inovação no agro não é apenas tecnologia de ponta, é sobre resolver gargalos produtivos.
        
        **Pontos Chave:**
        1. **Mentalidade:** Saia da visão apenas produtivista para a visão de gestão.
        2. **Ferramentas:** Use o Business Model Canvas adaptado.
        3. **Validação:** Teste pequeno antes de escalar na lavoura inteira.
        
        > *"O produtor rural não compra softwares, ele compra soluções para dores que tiram o sono dele."*
        """,
        "materiais": [
            {"tipo": "PDF", "nome": "Manual do Jovem Empreendedor Rural (Gov.br)", "url": "https://www.gov.br/mdh/pt-br/assuntos/noticias/2020-2/julho/Manualdojovemempreendedorrural.pdf"},
            {"tipo": "PDF", "nome": "Estado da Agricultura Digital (Embrapa/Sebrae)", "url": "https://sebrae.com.br/Sebrae/Portal%20Sebrae/UFs/RN/Anexos/Estado_atual_da_agricultura_digital_no_Brasil.pdf"},
            {"tipo": "Vídeo", "nome": "Webinar: Estratégias para Micro e Pequenas Empresas", "url": "https://www.youtube.com/watch?v=pNPX4AVYV-c"},
            {"tipo": "Vídeo", "nome": "Aula SENAR: Empreendedorismo Rural", "url": "https://www.youtube.com/watch?v=8k23veR6kuI"}
        ]
    },
    2: {"nome": "Formação Sociocultural e Sustentável", "status": "Bloqueado"},
    3: {"nome": "Introdução ao Curso de Engenharia Agronômica", "status": "Bloqueado"},
    4: {"nome": "Sustentabilidade, Diversidade e Desafios Globais", "status": "Bloqueado"},
    # ... Adicionaríamos até a 60 aqui
}

# --- LÓGICA DE ESTADO (SALVAR PROGRESSO) ---
if 'concluidas' not in st.session_state:
    st.session_state.concluidas = []

def marcar_concluido(id_disciplina):
    if id_disciplina not in st.session_state.concluidas:
        st.session_state.concluidas.append(id_disciplina)
        st.toast(f'Parabéns! Disciplina {id_disciplina} concluída!', icon="🎉")

# --- BARRA LATERAL (NAVEGAÇÃO) ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/tractor.png", width=80)
    st.title("Agronomia Premium")
    st.caption("Coordenação Pedagógica Virtual")
    
    # Cálculo de Progresso
    total_disciplinas = 60 # Fixo conforme seu plano
    progresso = len(st.session_state.concluidas) / total_disciplinas
    st.write(f"**Progresso Geral:** {int(progresso * 100)}%")
    st.progress(progresso)
    
    st.divider()
    
    st.subheader("📚 Grade Curricular")
    
    # Menu de Seleção
    disciplina_selecionada_id = st.selectbox(
        "Navegar para:",
        options=list(course_data.keys()),
        format_func=lambda x: f"{x}. {course_data[x]['nome']}"
    )

# --- ÁREA PRINCIPAL ---
disciplina = course_data[disciplina_selecionada_id]

st.title(f"🚜 {disciplina['nome']}")

if disciplina['status'] == "Bloqueado":
    st.warning("🔒 Esta disciplina ainda não foi liberada pelo coordenador. Complete as anteriores ou aguarde a próxima sprint.")
    st.info("Nosso curso é modular: focamos em aprender bem uma matéria por vez.")

else:
    # Layout da Aula Ativa
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📖 Aula Teórica")
        st.markdown(disciplina['conteudo'])
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.subheader("📺 Vídeo Aula Destaque")
        # Exemplo de embed de vídeo (usando um placeholder se o link não for direto)
        st.video("https://www.youtube.com/watch?v=8k23veR6kuI") 

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📂 Material Didático")
        st.write("Baixe os PDFs e assista aos materiais complementares:")
        
        for material in disciplina['materiais']:
            icon = "📄" if material['tipo'] == "PDF" else "▶️"
            st.markdown(f"**{icon} [{material['nome']}]({material['url']})**")
        
        st.divider()
        
        st.subheader("✅ Validação")
        is_completed = disciplina_selecionada_id in st.session_state.concluidas
        
        if is_completed:
            st.success("Disciplina Concluída!")
        else:
            if st.button("Marcar Aula como Concluída"):
                marcar_concluido(disciplina_selecionada_id)
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- RODAPÉ ---
st.divider()
st.caption("Desenvolvido para o Curso de Agronomia - Módulo 1/60 - Sistema Inteligente de Ensino")

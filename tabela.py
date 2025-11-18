#Tabela inicial, usando apenas os dados fornecidos primeiramente pelo DeepSeek.
#Resultados são impressos no terminal.

import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

class LLMComparator:
    def __init__(self):
        self.models = {
            'ChatGPT (GPT-4)': {
                'Overall Score': 85,
                'IFEval': 85,
                'BBH': 87,
                'MATH': 75,
                'GPQA': 80,
                'MuSR': 80,
                'MMLU-Pro': 85,
                'CO2_Emissions': 4.3  # g por consulta
            },
            'DeepSeek-V2': {
                'Overall Score': 78,
                'IFEval': 80,
                'BBH': 78,
                'MATH': 73,
                'GPQA': 70,
                'MuSR': 75,
                'MMLU-Pro': 70,
                'CO2_Emissions': 1.8  # g por consulta
            }
        }
        
        self.criteria = [
            'Overall Score', 'IFEval', 'BBH', 'MATH', 
            'GPQA', 'MuSR', 'MMLU-Pro'
        ]
    
    def display_comparison_table(self):
        """Exibe tabela comparativa formatada"""
        table_data = []
        headers = ['Critério', 'ChatGPT (GPT-4)', 'DeepSeek-V2', 'Diferença']
        
        for criterion in self.criteria:
            chatgpt_score = self.models['ChatGPT (GPT-4)'][criterion]
            deepseek_score = self.models['DeepSeek-V2'][criterion]
            difference = chatgpt_score - deepseek_score
            
            table_data.append([
                criterion,
                f"{chatgpt_score}%",
                f"{deepseek_score}%",
                f"{difference:+.1f}%"
            ])
        
        # Adiciona emissões de CO2 (dados brutos)
        chatgpt_co2 = self.models['ChatGPT (GPT-4)']['CO2_Emissions']
        deepseek_co2 = self.models['DeepSeek-V2']['CO2_Emissions']
        co2_reduction = ((chatgpt_co2 - deepseek_co2) / chatgpt_co2) * 100
        
        table_data.append([
            'CO2 Emissions',
            f"{chatgpt_co2}g",
            f"{deepseek_co2}g",
            f"-{co2_reduction:.1f}%"
        ])
        
        print("🔍 COMPARAÇÃO DETALHADA: ChatGPT vs DeepSeek")
        print("=" * 60)
        print(tabulate(table_data, headers=headers, tablefmt='grid'))
        print("\n" + "=" * 60)
    
    def create_radar_chart(self):
        """Cria gráfico radar para comparação visual"""
        criteria = self.criteria[:-1]  # Remove 'Overall Score'
        
        # Preparar dados para o radar
        chatgpt_scores = [self.models['ChatGPT (GPT-4)'][c] for c in criteria]
        deepseek_scores = [self.models['DeepSeek-V2'][c] for c in criteria]
        
        # Fechar o radar plot
        criteria = list(criteria)
        chatgpt_scores = chatgpt_scores + [chatgpt_scores[0]]
        deepseek_scores = deepseek_scores + [deepseek_scores[0]]
        criteria = criteria + [criteria[0]]
        
        angles = np.linspace(0, 2*np.pi, len(criteria), endpoint=False).tolist()
        angles += angles[:1]  # Fechar o círculo
        
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
        
        ax.plot(angles, chatgpt_scores, 'o-', linewidth=2, label='ChatGPT (GPT-4)', color='#10a37f')
        ax.fill(angles, chatgpt_scores, alpha=0.25, color='#10a37f')
        
        ax.plot(angles, deepseek_scores, 'o-', linewidth=2, label='DeepSeek-V2', color='#ff6b35')
        ax.fill(angles, deepseek_scores, alpha=0.25, color='#ff6b35')
        
        ax.set_thetagrids(np.degrees(angles[:-1]), criteria)
        ax.set_ylim(0, 100)
        ax.set_yticks([20, 40, 60, 80, 100])
        ax.grid(True)
        
        plt.title('Comparação de Desempenho: ChatGPT vs DeepSeek\n', size=14, fontweight='bold')
        plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
        plt.tight_layout()
        plt.show()
    
    def create_bar_chart(self):
        """Cria gráfico de barras para comparação lado a lado"""
        criteria = self.criteria[:-1]  # Remove 'Overall Score'
        
        chatgpt_scores = [self.models['ChatGPT (GPT-4)'][c] for c in criteria]
        deepseek_scores = [self.models['DeepSeek-V2'][c] for c in criteria]
        
        x = np.arange(len(criteria))
        width = 0.35
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        bars1 = ax.bar(x - width/2, chatgpt_scores, width, label='ChatGPT (GPT-4)', color='#10a37f', alpha=0.8)
        bars2 = ax.bar(x + width/2, deepseek_scores, width, label='DeepSeek-V2', color='#ff6b35', alpha=0.8)
        
        ax.set_xlabel('Critérios de Avaliação')
        ax.set_ylabel('Pontuação (%)')
        ax.set_title('Comparação Detalhada por Critério')
        ax.set_xticks(x)
        ax.set_xticklabels(criteria, rotation=45, ha='right')
        ax.legend()
        ax.set_ylim(0, 100)
        
        # Adicionar valores nas barras
        for bar in bars1:
            height = bar.get_height()
            ax.annotate(f'{height}%',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3),
                       textcoords="offset points",
                       ha='center', va='bottom')
        
        for bar in bars2:
            height = bar.get_height()
            ax.annotate(f'{height}%',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3),
                       textcoords="offset points",
                       ha='center', va='bottom')
        
        plt.tight_layout()
        plt.show()
    
    def environmental_impact_comparison(self):
        """Mostra comparação de impacto ambiental"""
        chatgpt_co2 = self.models['ChatGPT (GPT-4)']['CO2_Emissions']
        deepseek_co2 = self.models['DeepSeek-V2']['CO2_Emissions']
        
        reduction = ((chatgpt_co2 - deepseek_co2) / chatgpt_co2) * 100
        efficiency_ratio = chatgpt_co2 / deepseek_co2
        
        print("🌱 ANÁLISE DE IMPACTO AMBIENTAL")
        print("=" * 50)
        print(f"ChatGPT (GPT-4): {chatgpt_co2}g CO₂ por consulta")
        print(f"DeepSeek-V2: {deepseek_co2}g CO₂ por consulta")
        print(f"Redução: {reduction:.1f}% menos emissões")
        print(f"Eficiência: DeepSeek é {efficiency_ratio:.1f}x mais eficiente")
        print("\n💡 Interpretação:")
        print("- DeepSeek emite aproximadamente 58% menos CO₂ que ChatGPT")
        print("- Arquitetura Mixture of Experts (MoE) é mais sustentável")
        print("- Impacto significativo quando escalado para milhões de usuários")
    
    def recommendation_engine(self, user_priority):
        """
        Sistema de recomendação baseado na prioridade do usuário
        """
        priorities = {
            'performance': ['ChatGPT (GPT-4)', 'Desempenho máximo em todas as tarefas'],
            'efficiency': ['DeepSeek-V2', 'Excelente equilíbrio entre desempenho e eficiência'],
            'environment': ['DeepSeek-V2', 'Menor impacto ambiental e alta eficiência energética'],
            'cost': ['DeepSeek-V2', 'Provavelmente mais econômico para operação em escala']
        }
        
        if user_priority in priorities:
            recommendation, reason = priorities[user_priority]
            print(f"\n🎯 RECOMENDAÇÃO PARA PRIORIDADE: {user_priority.upper()}")
            print("=" * 50)
            print(f"Modelo Recomendado: {recommendation}")
            print(f"Motivo: {reason}")
            
            if user_priority == 'performance':
                print("\n⚠️  Consideração: Maior consumo energético e emissões de CO₂")
            elif user_priority in ['efficiency', 'environment', 'cost']:
                print("\n✅ Vantagem: Sustentável e econômico, com desempenho competitivo")
        else:
            print("Prioridade não reconhecida. Use: performance, efficiency, environment ou cost")

def main():
    comparator = LLMComparator()
    
    while True:
        print("\n" + "="*60)
        print("🤖 COMPARADOR DE LLMs: ChatGPT vs DeepSeek")
        print("="*60)
        print("1. 📊 Ver Tabela Comparativa")
        print("2. 📈 Gráfico Radar (Visual)")
        print("3. 📊 Gráfico de Barras")
        print("4. 🌱 Análise de Impacto Ambiental")
        print("5. 💡 Sistema de Recomendação")
        print("6. 🚪 Sair")
        print("="*60)
        
        choice = input("\nEscolha uma opção (1-6): ").strip()
        
        if choice == '1':
            comparator.display_comparison_table()
        elif choice == '2':
            comparator.create_radar_chart()
        elif choice == '3':
            comparator.create_bar_chart()
        elif choice == '4':
            comparator.environmental_impact_comparison()
        elif choice == '5':
            print("\nPrioridades disponíveis: performance, efficiency, environment, cost")
            priority = input("Digite sua prioridade principal: ").strip().lower()
            comparator.recommendation_engine(priority)
        elif choice == '6':
            print("Obrigado por usar o comparador! 👋")
            break
        else:
            print("Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    # Instalação de dependências necessárias (executar no terminal)
    # pip install matplotlib numpy tabulate
    
    main()
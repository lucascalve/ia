def generate_html_page():
    html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comparação de LLMs: ChatGPT, DeepSeek e Gemini</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            color: #333;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
            padding: 30px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }

        .controls {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }

        .view-btn {
            background: white;
            border: none;
            padding: 12px 25px;
            border-radius: 50px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        .view-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        }

        .view-btn.active {
            background: #ff6b35;
            color: white;
        }

        .tables-container {
            display: flex;
            flex-direction: column;
            gap: 30px;
        }

        .table-wrapper {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
        }

        .table-wrapper:hover {
            transform: translateY(-5px);
        }

        .table-title {
            text-align: center;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 2px solid #f0f0f0;
            font-size: 1.5em;
            color: #333;
        }

        .table-title.deepseek {
            color: #10a37f;
            border-color: #10a37f;
        }

        .table-title.chatgpt {
            color: #ff6b35;
            border-color: #ff6b35;
        }

        .table-title.gemini {
            color: #4285f4;
            border-color: #4285f4;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 10px;
        }

        th {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }

        td {
            padding: 15px;
            border-bottom: 1px solid #f0f0f0;
        }

        tr:nth-child(even) {
            background-color: #f8f9fa;
        }

        tr:hover {
            background-color: #e9ecef;
        }

        .range-value {
            font-weight: bold;
        }

        .co2-value {
            font-weight: bold;
            color: #e74c3c;
        }

        .single-view .table-wrapper {
            width: 100%;
        }

        .side-by-side-view {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 20px;
        }

        .side-by-side-view .table-wrapper {
            margin-bottom: 0;
        }

        /* Estilos para o sumário */
        .summary {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-top: 30px;
        }

        .summary h2 {
            text-align: center;
            margin-bottom: 25px;
            color: #333;
            font-size: 1.8em;
        }

        .summary-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .summary-item {
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            background: #f8f9fa;
            transition: transform 0.3s ease;
        }

        .summary-item:hover {
            transform: translateY(-5px);
        }

        .summary-value {
            font-size: 2em;
            font-weight: bold;
            margin: 10px 0;
        }

        .chatgpt-color {
            color: #ff6b35;
        }

        .deepseek-color {
            color: #10a37f;
        }

        .gemini-color {
            color: #4285f4;
        }

        .recommendation {
            background: linear-gradient(135deg, #ffeaa7, #fab1a0);
            padding: 25px;
            border-radius: 15px;
            margin-top: 20px;
            text-align: center;
        }

        .recommendation h3 {
            color: #2d3436;
            margin-bottom: 10px;
        }

        .observation {
            background: #e3f2fd;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            border-left: 5px solid #2196f3;
        }

        .observation h4 {
            color: #1565c0;
            margin-bottom: 10px;
        }

        .footer {
            text-align: center;
            color: white;
            margin-top: 40px;
            opacity: 0.8;
        }

        @media (max-width: 768px) {
            .side-by-side-view {
                grid-template-columns: 1fr;
            }
            
            .controls {
                flex-direction: column;
                align-items: center;
            }
            
            .view-btn {
                width: 80%;
            }
            
            .summary-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 Comparação de LLMs: ChatGPT, DeepSeek e Gemini</h1>
            <p>Análise baseada em diferentes fontes de dados e benchmarks</p>
        </div>

        <div class="controls">
            <button class="view-btn active" onclick="showView('deepseek')">Tabela DeepSeek</button>
            <button class="view-btn" onclick="showView('chatgpt')">Tabela ChatGPT</button>
            <button class="view-btn" onclick="showView('gemini')">Tabela Gemini</button>
            <button class="view-btn" onclick="showView('side-by-side')">Visualização Lado a Lado</button>
        </div>

        <div class="tables-container single-view" id="tables-container">
            <!-- Tabela DeepSeek -->
            <div class="table-wrapper" id="deepseek-table">
                <h2 class="table-title deepseek">Tabela DeepSeek</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Critério de Avaliação</th>
                            <th>ChatGPT (GPT-4)</th>
                            <th>DeepSeek</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><b>Média Ponderada da Pontuação</b></td>
                            <td><b>85%</b></td>
                            <td><b>78%</b></td>
                        </tr>
                        <tr>
                            <td><b>Instruction Following Evaluation (IFEval)</b></td>
                            <td><b>85%</b></td>
                            <td><b>80%</b></td>
                        </tr>
                        <tr>
                            <td><b>Big Bench Hard (BBH)</b></td>
                            <td><b>87%</b></td>
                            <td><b>80%</b></td>
                        </tr>
                        <tr>
                            <td><b>Mathematics Aptitude Test of Heuristics (MATH) level 5</b></td>
                            <td><b>70%</b></td>
                            <td><b>75%</b></td>
                        </tr>
                        <tr>
                            <td><b>Graduate-Level Google-Proof Q&A (GPQA)</b></td>
                            <td><b>80%</b></td>
                            <td><b>70%</b></td>
                        </tr>
                        <tr>
                            <td><b>Multistep Score Reasoning (MuSR)</b></td>
                            <td><b>80%</b></td>
                            <td><b>75%</b></td>
                        </tr>
                        <tr>
                            <td><b>Massive Multitask Language Understanding - Professional (MMLU-Pro)</b></td>
                            <td><b>85%</b></td>
                            <td><b>Não Divulgado</b></td>
                        </tr>
                        <tr>
                            <td><b>Emissões de CO<sub>2</sub></b></td>
                            <td><b class="co2-value">4.3g por consulta</b></td>
                            <td><b class="co2-value">1.8g por consulta</b></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Tabela ChatGPT (inicialmente oculta) -->
            <div class="table-wrapper" id="chatgpt-table" style="display: none;">
                <h2 class="table-title chatgpt">Tabela ChatGPT</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Critério de Avaliação</th>
                            <th>ChatGPT</th>
                            <th>DeepSeek</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><b>Média Ponderada da Pontuação</b></td>
                            <td><b>85%</b></td>
                            <td><b>80%</b></td>
                        </tr>
                        <tr>
                            <td><b>Instruction Following Evaluation (IFEval)</b></td>
                            <td><b>90%</b></td>
                            <td><b>80%</b></td>
                        </tr>
                        <tr>
                            <td><b>Big Bench Hard (BBH)</b></td>
                            <td><b>87%</b></td>
                            <td><b>82%</b></td>
                        </tr>
                        <tr>
                            <td><b>Mathematics Aptitude Test of Heuristics (MATH) - Nível 5</b></td>
                            <td><b>80%</b></td>
                            <td><b>75%</b></td>
                        </tr>
                        <tr>
                            <td><b>Graduate-Level Google-Proof Q&A (GPQA)</b></td>
                            <td><b>88%</b></td>
                            <td><b>85%</b></td>
                        </tr>
                        <tr>
                            <td><b>Multistep Score Reasoning (MuSR)</b></td>
                            <td><b>86%</b></td>
                            <td><b>78%</b></td>
                        </tr>
                        <tr>
                            <td><b>Massive Multitask Language Understanding - Professional (MMLU-Pro)</b></td>
                            <td><b>92%</b></td>
                            <td><b>85%</b></td>
                        </tr>
                        <tr>
                            <td><b>Emissões de CO<sub>2</sub></b></td>
                            <td><b class="co2-value">0.45 kg por resposta</b></td>
                            <td><b class="co2-value">0.60 kg por resposta</b></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Tabela Gemini (inicialmente oculta) -->
            <div class="table-wrapper" id="gemini-table" style="display: none;">
                <h2 class="table-title gemini">Tabela Gemini</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Critério</th>
                            <th>ChatGPT</th>
                            <th>DeepSeek</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><b>Média ponderada da pontuação dos outros critérios</b></td>
                            <td><b>90%</b></td>
                            <td><b>80%</b></td>
                        </tr>
                        <tr>
                            <td><b>Instruction Following Evaluation (IFEval)</b></td>
                            <td><b>90%</b></td>
                            <td><b>85%</b></td>
                        </tr>
                        <tr>
                            <td><b>Big Bench Hard (BBH)</b></td>
                            <td><b>85%</b></td>
                            <td><b>75%</b></td>
                        </tr>
                        <tr>
                            <td><b>Mathematics Aptitude Test of Heuristics (MATH) - Nível 5</b></td>
                            <td><b>60%</b></td>
                            <td><b>50%</b></td>
                        </tr>
                        <tr>
                            <td><b>Graduate-Level Google-Proof Q&A (GPQA)</b></td>
                            <td><b>60%</b></td>
                            <td><b>50%</b></td>
                        </tr>
                        <tr>
                            <td><b>Multistep Score Reasoning (MuSR)</b></td>
                            <td><b>85%</b></td>
                            <td><b>80%</b></td>
                        </tr>
                        <tr>
                            <td><b>Massive Multitask Language Understanding - Professional (MMLU-Pro)</b></td>
                            <td><b>90%</b></td>
                            <td><b>80%</b></td>
                        </tr>
                        <tr>
                            <td><b>Emissões de gás carbônico (CO₂)</b></td>
                            <td><b>Não Divulgado</b></td>
                            <td><b>Não Divulgado</b></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Resumo e Recomendações -->
        <div class="summary">
            <h2>🎯 Análise e Recomendações</h2>
            <div class="summary-grid">
                <div class="summary-item">
                    <h3>🏆 Desempenho Geral</h3>
                    <div class="summary-value chatgpt-color">ChatGPT</div>
                    <p>Lidera na maioria dos critérios de desempenho</p>
                </div>
                <div class="summary-item">
                    <h3>🌱 Sustentabilidade</h3>
                    <div class="summary-value deepseek-color">DeepSeek</div>
                    <p>Menor consumo energético e emissões</p>
                </div>
                <div class="summary-item">
                    <h3>🧮 Capacidade Matemática</h3>
                    <div class="summary-value deepseek-color">DeepSeek</div>
                    <p>Melhor desempenho em MATH (Tabela DeepSeek)</p>
                </div>
                <div class="summary-item">
                    <h3>💵 Custo-Benefício</h3>
                    <div class="summary-value deepseek-color">DeepSeek</div>
                    <p>Melhor para operação em escala com orçamento limitado</p>
                </div>
            </div>

            <div class="recommendation">
                <h3>💡 Recomendação por Caso de Uso</h3>
                <p><strong>ChatGPT (GPT-4):</strong> Quando a máxima performance é essencial, especialmente para tarefas de linguagem e compreensão geral</p>
                <p><strong>DeepSeek-V2:</strong> Para aplicações que exigem raciocínio lógico e matemático, ou quando a eficiência energética é prioridade</p>
            </div>
            
            <div class="observation">
                <h4>👨‍💻 Observação dos Especialistas</h4>
                <p>Especialistas em IA geralmente preferem o <strong>ChatGPT</strong> para tarefas de geração de textos, resumos e compreensão geral de linguagem, devido à sua fluência e coerência textual. Por outro lado, o <strong>DeepSeek</strong> é frequentemente preferido para operações que envolvem lógica complexa, raciocínio matemático e tarefas que exigem pensamento analítico estruturado.</p>
            </div>
        </div>

        <div class="footer">
            <p>📊 Dados baseados em diferentes fontes e benchmarks | Última atualização: 2024</p>
        </div>
    </div>

    <script>
        function showView(viewType) {
            // Atualizar botões ativos
            const buttons = document.querySelectorAll('.view-btn');
            buttons.forEach(btn => btn.classList.remove('active'));
            
            // Ativar o botão clicado
            event.target.classList.add('active');
            
            const container = document.getElementById('tables-container');
            const deepseekTable = document.getElementById('deepseek-table');
            const chatgptTable = document.getElementById('chatgpt-table');
            const geminiTable = document.getElementById('gemini-table');
            
            // Reset para modo single view
            container.className = 'tables-container single-view';
            deepseekTable.style.display = 'none';
            chatgptTable.style.display = 'none';
            geminiTable.style.display = 'none';
            
            switch(viewType) {
                case 'deepseek':
                    deepseekTable.style.display = 'block';
                    break;
                case 'chatgpt':
                    chatgptTable.style.display = 'block';
                    break;
                case 'gemini':
                    geminiTable.style.display = 'block';
                    break;
                case 'side-by-side':
                    container.className = 'tables-container side-by-side-view';
                    deepseekTable.style.display = 'block';
                    chatgptTable.style.display = 'block';
                    geminiTable.style.display = 'block';
                    break;
            }
        }
    </script>
</body>
</html>
"""
    return html_content

def save_html_file(content, filename="comparacao_llms.html"):
    """Salva o conteúdo HTML em um arquivo"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"✅ Arquivo '{filename}' gerado com sucesso!")
        print(f"📁 Abra o arquivo no seu navegador para visualizar a comparação.")
    except Exception as e:
        print(f"❌ Erro ao salvar o arquivo: {e}")

def main():
    """Função principal que gera a página HTML"""
    print("🚀 Gerando página de comparação de LLMs...")
    
    # Gerar o conteúdo HTML
    html_content = generate_html_page()
    
    # Salvar o arquivo
    save_html_file(html_content)
    
    print("\n📋 Resumo do conteúdo gerado:")
    print("• 3 tabelas comparativas (DeepSeek, ChatGPT, Gemini)")
    print("• Sistema de visualização com botões de alternância")
    print("• Modo de visualização lado a lado")
    print("• Sumário com análise e recomendações")
    print("• Design responsivo e moderno")

if __name__ == "__main__":
    main()
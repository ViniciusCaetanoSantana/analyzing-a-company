import pandas as pd

servicos = pd.read_excel('BaseServiçosPrestados.xlsx')
funcionarios = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes = pd.read_csv('CadastroClientes.csv', sep=';')

# print(servicos)
# print(funcionarios)
# print(clientes)


salario_total_gasto = sum(funcionarios['Salario Base']) + sum(funcionarios['Impostos']) + sum(funcionarios['Beneficios']) + sum(funcionarios['VT']) + sum(funcionarios['VR'])
print(f'o total de gasto com salario foi de {salario_total_gasto:,.2f}') # total salary expense

print('=-'*15)

faturamento = servicos.merge(clientes) #sempre pegar a tabela com valores unicos a adicionar na tabela que pode ter valores duplicados (id do cliente)
faturamento = faturamento.drop(columns=['Cliente', 'ID Funcionário', 'Codigo do Servico'])
faturamento['Total Faturamento'] = faturamento['Valor Contrato Mensal'] * faturamento['Tempo Total de Contrato (Meses)']
faturamento_total = sum(faturamento['Total Faturamento'])
print(f'o faturamento total foi de {faturamento_total:,.2f}') # total billing

print('=-'*15)

porcentagem_funcionarios_com_servicos = ((len(servicos['ID Funcionário'].unique())) / (len(funcionarios['ID Funcionário'].unique())))
print(f'a porcentagem de funcionarios que fizeram ao menos um contrato é de {porcentagem_funcionarios_com_servicos:.2%}') # percentage of employees who have at least one contract

print('=-'*15)

contratos_por_area = servicos[['ID Funcionário']].merge(funcionarios[['ID Funcionário', 'Area']], on='ID Funcionário')
quantidades_area = contratos_por_area['Area'].value_counts()
print(f'''nossos contratos por area estão assim:
{quantidades_area}''') # contracts by area

print('=-'*15)

funcionarios_por_area = funcionarios['Area'].value_counts()
print(f'''nossos funcionarios estão distribuidos assim:
{funcionarios_por_area}''') # distribution of employees by area

print('=-'*15)

media_mensal = clientes['Valor Contrato Mensal'].mean()
print(f'a média de faturamento mensal é de {media_mensal:,.2f}') # average monthly billing
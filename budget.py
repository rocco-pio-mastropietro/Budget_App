##
#  Questo modulo definisce la classe Category.
#

## E' in grado di instanziare oggetti basati su
#  diverse categorie di budget.
class Category:
  ## Costruisce gli oggetti, che ricevono come 
  #  argomento il nome della categoria.
  #  @param category il nome della categoria
  #
  def __init__(self, category):
    self.ledger = []
    self.name = category

  ## Visualizza stringhe leggibili.
  #  @return una riga di titolo dove il nome della 
  #  categoria è centrato in una riga di caratteri *.
  #  Una lista delle transazioni nel ledger.
  #  Una riga che mostra il totale della categoria.
  #
  def __str__(self):
    header = (30 - len(self.name)) // 2 * "*" + self.name + (30 - len(self.name)) // 2 * "*" + "\n"

    body = ""
    for item in self.ledger:
      body += f"%-23.23s%7.2f\n" %(item["description"], item["amount"])
    
    total = str(self.get_balance())
      
    return f"{header}{body}Total: {total}"

  ## Metodo di deposito che accetta un valore e una 
  #  descrizione. Il metodo aggiunge un oggetto alla 
  #  lista ledger. 
  #  @param amount il valore
  #  @param description la descrizione. Se non è
  #  data alcuna descrizione, sarà una stringa vuota
  #  come default.
  #
  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  ## Un metodo di prelievo simile al metodo deposit, 
  #  in cui il valore dato come argomento è salvato 
  #  come valore negativo. Se non ci sono abbastanza 
  #  fondi, nulla sarà aggiunto al ledger.
  #  @param amount il valore
  #  @param description la descrizione. Se non è
  #  data alcuna descrizione, sarà una stringa vuota
  #  come default.
  #  @return True se il prelievo ha avuto atto, e 
  #  False altrimenti.
  #
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False
  ## Un metodo per ottenere la giacenza attuale 
  #  @return l'ammontare nella categoria del budget 
  #  basato su depositi e prelievi che hanno avuto 
  #  luogo.
  #
  def get_balance(self):
    total_amount = 0
    for item in self.ledger:
        total_amount += item["amount"]
    return total_amount

  ## Un metodo di trasferimento che accetta un 
  #  ammontare e un'altra categoria come argomenti. 
  #  Il metodo aggunge un prelievo con l'ammontare e 
  #  una descrizione. Il metodo aggiunge un deposito 
  #  all'altra categoria del budget con l'ammontare 
  #  e una descrizione. Se non ci sono abbastanza 
  #  fondi, nulla sarà aggiunto a nessuno dei due 
  #  ledger.
  #  @return True se il trasferimento ha avuto 
  #  luogo, e False altrimenti.
  #
  def transfer(self, amount, new_category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {new_category.name}")
      new_category.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False

  ## Un metodo che accetta un ammontare come
  #  argomento.
  #  @return False se l'ammontare è più grande del
  #  saldo della categoria del budget e True
  #  altrimenti.
  #
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True
      
## Una funzione che prende una lista di max 4
#  categorie come argomento.
#  @return una stringa che è un grafico a barre.
#
def create_spend_chart(categories):
  total_withdraw = 0
  for category in categories:
    for item in category.ledger:
      if item["amount"] < 0:
        total_withdraw += item["amount"]

  i = 0
  withdraw_i = 0
  percentage_withdraw_i = 0
  list_percentages_withdraw = []
  
  while i < len(categories):
    for item in categories[i].ledger:
      if item["amount"] < 0:
        withdraw_i += item["amount"]
    percentage_withdraw_i = round(withdraw_i / total_withdraw * 100)
    list_percentages_withdraw.append(percentage_withdraw_i)
    i += 1
    withdraw_i = 0

  title = "Percentage spent by category"
  column_labels = ["100|", " 90|", " 80|", " 70|", " 60|", " 50|", " 40|", " 30|", " 20|", " 10|", "  0|"]
  column_percentages = ["", "", "", "", "", "", "", "", "", "", ""]
  horizontal_line = 4 * " " + (3 * len(list_percentages_withdraw) + 1) * "-"

  for percentage in list_percentages_withdraw:
    if percentage == "100":
      for i in range(11):
        column_percentages[i] += " o "
    elif percentage < 100 and percentage >= 90:
      column_percentages[0] += "   "
      for i in range(1, 11):
        column_percentages[i] += " o "
    elif percentage < 90 and percentage >= 80:
      for i in range(2):
        column_percentages[i] += "   "
      for i in range(2, 11):
        column_percentages[i] += " o "
    elif percentage < 80 and percentage >= 70:
      for i in range(3):
        column_percentages[i] += "   "
      for i in range(3, 11):
        column_percentages[i] += " o "
    elif percentage < 70 and percentage >= 60:
      for i in range(4):
        column_percentages[i] += "   "
      for i in range(4, 11):
        column_percentages[i] += " o "
    elif percentage < 60 and percentage >= 50:
      for i in range(5):
        column_percentages[i] += "   "
      for i in range(5, 11):
        column_percentages[i] += " o "
    elif percentage < 50 and percentage >= 40:
      for i in range(6):
        column_percentages[i] += "   "
      for i in range(6, 11):
        column_percentages[i] += " o "
    elif percentage < 40 and percentage >= 30:
      for i in range(7):
        column_percentages[i] += "   "
      for i in range(7, 11):
        column_percentages[i] += " o "
    elif percentage < 30 and percentage >= 20:
      for i in range(8):
        column_percentages[i] += "   "
      for i in range(8, 11):
        column_percentages[i] += " o "
    elif percentage < 20 and percentage >= 10:
      for i in range(9):
        column_percentages[i] += "   "
      for i in range(9, 11):
        column_percentages[i] += " o "
    else:
      for i in range(10):
        column_percentages[i] += "   "
      column_percentages[10] += " o "
    
  chart = f"{title}\n{column_labels[0]}{column_percentages[0]} \n{column_labels[1]}{column_percentages[1]} \n{column_labels[2]}{column_percentages[2]} \n{column_labels[3]}{column_percentages[3]} \n{column_labels[4]}{column_percentages[4]} \n{column_labels[5]}{column_percentages[5]} \n{column_labels[6]}{column_percentages[6]} \n{column_labels[7]}{column_percentages[7]} \n{column_labels[8]}{column_percentages[8]} \n{column_labels[9]}{column_percentages[9]} \n{column_labels[10]}{column_percentages[10]} \n{horizontal_line}"

  column_categories = []
  len_column_categories = max(len(categories[0].name), len(categories[1].name), len(categories[2].name))
  for _ in range(len_column_categories):
    column_categories.append("")
  for category in categories:
    for j in range(len_column_categories):
      try:
        column_categories[j] += f" {category.name[j]} "
      except IndexError:
        column_categories[j] += "   "
  for j in range(len_column_categories):
    chart += f"\n    {column_categories[j]} "
    
  return chart
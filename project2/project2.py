from abc import ABC, abstractmethod
import requests
import tkinter as tk
from tkinter import ttk

class CurrencyConverter(ABC):
    @abstractmethod
    def convert(self, amount, from_currency, to_currency):
        pass


class OpenExchangeRatesConverter(CurrencyConverter):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://openexchangerates.org/api/"
        self.rates = {}
        self.update_rates()

    def update_rates(self):
        url = f"{self.base_url}latest.json?app_id={self.api_key}"
        response = requests.get(url)
        data = response.json()
        self.rates = data['rates']

    def convert(self, amount, from_currency, to_currency):
        if from_currency != 'USD':
            amount = amount / self.rates[from_currency]
        return amount * self.rates[to_currency]


class USDAdapter(CurrencyConverter):
    def __init__(self, converter):
        self.converter = converter

    def convert(self, amount, from_currency, to_currency):
        return self.converter.convert(amount, from_currency, to_currency)

class EURAdapter(CurrencyConverter):
    def __init__(self, converter):
        self.converter = converter

    def convert(self, amount, from_currency, to_currency):
        return self.converter.convert(amount, from_currency, to_currency)

class GBPAdapter(CurrencyConverter):
    def __init__(self, converter):
        self.converter = converter

    def convert(self, amount, from_currency, to_currency):
        return self.converter.convert(amount, from_currency, to_currency)

class JPYAdapter(CurrencyConverter):
    def __init__(self, converter):
        self.converter = converter

    def convert(self, amount, from_currency, to_currency):
        return self.converter.convert(amount, from_currency, to_currency)

class AUDAdapter(CurrencyConverter):
    def __init__(self, converter):
        self.converter = converter

    def convert(self, amount, from_currency, to_currency):
        return self.converter.convert(amount, from_currency, to_currency)
    

class CurrencyAdapterFactory:
    def __init__(self, api_key):
        self.converter = OpenExchangeRatesConverter(api_key)

    def get_adapter(self, currency):
        adapters = {
            'USD': USDAdapter(self.converter),
            'EUR': EURAdapter(self.converter),
            'GBP': GBPAdapter(self.converter),
            'JPY': JPYAdapter(self.converter),
            'AUD': AUDAdapter(self.converter)
        }
        return adapters.get(currency)


class CurrencyConverterApp:
    def __init__(self, root, factory):
        self.factory = factory
        self.root = root
        self.root.title("Currency Converter")

        self.amount_label = ttk.Label(root, text="Amount:")
        self.amount_label.grid(column=0, row=0, padx=10, pady=10)
        self.amount_entry = ttk.Entry(root)
        self.amount_entry.grid(column=1, row=0, padx=10, pady=10)

        self.from_currency_label = ttk.Label(root, text="From Currency:")
        self.from_currency_label.grid(column=0, row=1, padx=10, pady=10)
        self.from_currency_combobox = ttk.Combobox(root, values=['USD', 'EUR', 'GBP', 'JPY', 'AUD'])
        self.from_currency_combobox.grid(column=1, row=1, padx=10, pady=10)

        self.to_currency_label = ttk.Label(root, text="To Currency:")
        self.to_currency_label.grid(column=0, row=2, padx=10, pady=10)
        self.to_currency_combobox = ttk.Combobox(root, values=['USD', 'EUR', 'GBP', 'JPY', 'AUD'])
        self.to_currency_combobox.grid(column=1, row=2, padx=10, pady=10)

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

    def convert_currency(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_currency_combobox.get()
        to_currency = self.to_currency_combobox.get()

        adapter = self.factory.get_adapter(from_currency)
        if adapter:
            converted_amount = adapter.convert(amount, from_currency, to_currency)
            self.result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            self.result_label.config(text="Unsupported currency")


if __name__ == "__main__":
    api_key = "3a036e30fd614bf8bd87bc56b5291b6e" 
    factory = CurrencyAdapterFactory(api_key)

    root = tk.Tk()
    app = CurrencyConverterApp(root, factory)
    root.mainloop()

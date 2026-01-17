// Currency data with full names and country codes for flags
const CURRENCY_DATA = {
  'EUR': { name: 'Euro', country: 'eu' },
  'USD': { name: 'Amerikan Doları', country: 'us' },
  'GBP': { name: 'İngiliz Sterlini', country: 'gb' },
  'JPY': { name: 'Japon Yeni', country: 'jp' },
  'TRY': { name: 'Türk Lirası', country: 'tr' },
  'AUD': { name: 'Avustralya Doları', country: 'au' },
  'CAD': { name: 'Kanada Doları', country: 'ca' },
  'CHF': { name: 'İsviçre Frangı', country: 'ch' },
  'CNY': { name: 'Çin Yuanı', country: 'cn' },
  'SEK': { name: 'İsveç Kronu', country: 'se' },
  'NZD': { name: 'Yeni Zelanda Doları', country: 'nz' },
  'MXN': { name: 'Meksika Pesosu', country: 'mx' },
  'SGD': { name: 'Singapur Doları', country: 'sg' },
  'HKD': { name: 'Hong Kong Doları', country: 'hk' },
  'NOK': { name: 'Norveç Kronu', country: 'no' },
  'KRW': { name: 'Güney Kore Wonu', country: 'kr' },
  'INR': { name: 'Hindistan Rupisi', country: 'in' },
  'RUB': { name: 'Rus Rublesi', country: 'ru' },
  'BRL': { name: 'Brezilya Reali', country: 'br' },
  'ZAR': { name: 'Güney Afrika Randı', country: 'za' },
  'DKK': { name: 'Danimarka Kronu', country: 'dk' },
  'PLN': { name: 'Polonya Zlotisi', country: 'pl' },
  'THB': { name: 'Tayland Bahtı', country: 'th' },
  'MYR': { name: 'Malezya Ringiti', country: 'my' },
  'HUF': { name: 'Macar Forinti', country: 'hu' },
  'CZK': { name: 'Çek Kronu', country: 'cz' },
  'ILS': { name: 'İsrail Şekeli', country: 'il' },
  'CLP': { name: 'Şili Pesosu', country: 'cl' },
  'PHP': { name: 'Filipin Pesosu', country: 'ph' },
  'AED': { name: 'BAE Dirhemi', country: 'ae' },
  'SAR': { name: 'Suudi Riyali', country: 'sa' },
  'IDR': { name: 'Endonezya Rupisi', country: 'id' },
  'RON': { name: 'Romen Leyi', country: 'ro' },
  'BGN': { name: 'Bulgar Levası', country: 'bg' },
  'HRK': { name: 'Hırvat Kunası', country: 'hr' },
  'ISK': { name: 'İzlanda Kronu', country: 'is' }
};

// ülke kodunu bayrağa çeviren kısım
function getFlagEmoji(countryCode) {
  if (!countryCode) return '🏴';

  const codePoints = countryCode
    .toUpperCase()
    .split('')
    .map(char => 127397 + char.charCodeAt());
  return String.fromCodePoint(...codePoints);
}

// kur için bayrak emojisi
function getCurrencyFlag(currencyCode) {
  const countryCode = CURRENCY_DATA[currencyCode]?.country || currencyCode.substring(0, 2);
  return getFlagEmoji(countryCode);
}

// para biriminin tüm adını alır
function getCurrencyName(currencyCode) {
  return CURRENCY_DATA[currencyCode]?.name || currencyCode;
}

// numaralandırma
function formatCurrency(value, decimals = 4) {
  return parseFloat(value).toFixed(decimals);
}

// değer değiştiğinde döviz hesaplayıcı
function updateExchangeRate() {
  const amount = parseFloat(document.getElementById('amount')?.value) || 0;
  const fromCurrency = document.getElementById('from_currency')?.value;
  const toCurrency = document.getElementById('to_currency')?.value;

  if (amount && fromCurrency && toCurrency && window.rates) {
    const rate = window.rates[toCurrency] / window.rates[fromCurrency];
    const result = amount * rate;

    const rateDisplay = document.querySelector('.rate-value-large');
    if (rateDisplay) {
      rateDisplay.textContent = formatCurrency(result, 2);
    }
  }
}

// Toggle mobile menu
function toggleMobileMenu() {
  const mobileMenu = document.querySelector('.mobile-menu');
  mobileMenu.classList.toggle('active');
}

// scrollu dönüştürücü
function scrollToConverter(e) {
  e.preventDefault();
  const converter = document.getElementById('converter');
  if (converter) {
    converter.scrollIntoView({ behavior: 'smooth', block: 'start' });
    const mobileMenu = document.querySelector('.mobile-menu');
    if (mobileMenu) {
      mobileMenu.classList.remove('active');
    }
  }
}

// sayfa tanıtımı
document.addEventListener('DOMContentLoaded', function() {
  const amountInput = document.getElementById('amount');
  const fromSelect = document.getElementById('from_currency');
  const toSelect = document.getElementById('to_currency');


  // Mobile menu toggle
  const hamburger = document.querySelector('.hamburger');
  if (hamburger) {
    hamburger.addEventListener('click', toggleMobileMenu);
  }

  //hesapla scroll
  const calcButtons = document.querySelectorAll('.btn-calculate');
  calcButtons.forEach(btn => {
    btn.addEventListener('click', scrollToConverter);
  });
});

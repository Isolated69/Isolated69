const detailBtc = document.getElementById('btc-price')
const detailDoge = document.getElementById('doge-price')
const detailEth = document.getElementById('eth-price')
const detailXmr = document.getElementById('xmr-price')
const detailAda = document.getElementById('ada-price')

function loadPrices() {
    var xhr = new XMLHttpRequest()
    xhr.open('GET', 'data.json', true)

    xhr.onload = function() {
        if(this.status == 200) {
            var data = JSON.parse(this.responseText)
            detailBtc.textContent = data.cryptos.BTC
            detailDoge.textContent = data.cryptos.DOGE
            detailAda.textContent = data.cryptos.ADA
            detailXmr.textContent = data.cryptos.XMR
            detailEth.textContent = data.cryptos.ETH
        }
    }

    xhr.send()
}

setInterval(loadPrices, 1)
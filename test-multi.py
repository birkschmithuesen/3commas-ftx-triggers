import config
from py3cw.request import Py3CW

p3cw = Py3CW(
    key=config.TC_API_KEY,
    secret=config.TC_API_SECRET,
    request_options={
        'request_timeout': 30,
        'nr_of_retries': 1,
        'retry_status_codes': [502]
    }
)



error, bot_trigger = p3cw.request(
    entity = 'bots',
    action = 'start_new_deal',
    action_id = '8915934',
    payload = {
        'pair': 'USD_BTC-PERP'
    }
)
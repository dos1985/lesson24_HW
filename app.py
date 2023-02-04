import os
from typing import List, Dict, Callable, Tuple, Union, Iterator, Optional

from flask import Flask, request, Response

from utils import limit, unique, xfilter, lines, sort, xmap, regex

app: Flask = Flask(__name__)

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
DATA_DIR: str = os.path.join(BASE_DIR, "data")
CMD_DICT: Dict[str, Callable] = {
                                    'filter': xfilter,
                                    'map': xmap,
                                    'unique': unique,
                                    'sort': sort,
                                    'limit': limit,
                                    'regex': regex
                                }


@app.route("/perform_query", methods=['POST'])
def perform_query() -> Union[Response, Tuple[str, int]]:

    cmd1: Optional[str] = request.args.get('cmd1')
    value1: Optional[str] = request.args.get('value1')
    cmd2: Optional[str] = request.args.get('cmd2')
    value2: Optional[str] = request.args.get('value2')
    file_name: Optional[str] = request.args.get('file_name')

    path: str = f'{DATA_DIR}/{file_name}'

    if not os.path.exists(path):
        return '', 400

    if cmd1 is not None and value1 is not None:
        if cmd1 in CMD_DICT:
            res: Union[Iterator, List] = lines(path)
            res = list(CMD_DICT[cmd1](res, value1))
        else:
            return '', 400
    else:
        return '', 400

    if cmd2 is not None and value2 is not None:
        if cmd2 in CMD_DICT:
            res = list(CMD_DICT[cmd2](res, value2))
        else:
            return '', 400

    res_str: str = '\n'.join(res)

    return app.response_class(res_str, content_type="text/plain")

if __name__ == '__main__':
    debug = True
    app.run()
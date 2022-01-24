"""Here provides validation methods"""

import re


def valid_dob(data):
    """Expect dob format yyyy-mm-dd"""
    if isinstance(data, str):
        dob = re.search(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$', data)
        return dob
    return None


def valid_put_payload(parser):
    """Catch and validate put method payload"""
    parser.add_argument("full_name", type=str, required=True)
    parser.add_argument("dob", type=str, required=True)
    args = parser.parse_args()
    if not valid_dob(args['dob']):
        args["dob"] = "Expect dob format: yyyy-mm-dd"
        return args

    return args


def valid_post_payload(parser):
    """Catch and validate post method payload"""
    parser.add_argument("full_name", type=str)
    parser.add_argument("dob", type=str)
    args = parser.parse_args()

    return args

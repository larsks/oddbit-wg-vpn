import subprocess


def filter_wg_extract_pubkey(val):
    pubkey = subprocess.check_output(['wg', 'pubkey'],
                                     input=val,
                                     text=True,
                                     )
    return pubkey.strip()


class FilterModule:
    def filters(self):
        return {
            'wg_extract_pubkey': filter_wg_extract_pubkey,
        }

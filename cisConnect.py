import atexit
from pyVim.connect import Disconnect

from pyVim import connect


def connection(args):
    try:
        si = connect.ConnectNoSSL(host=args.host,
                                  user=args.user,
                                  pwd=args.password,
                                  port=int(args.port))
        atexit.register(Disconnect, si)
        print("No SSL Connection: warning!!")
    except Exception:
        raise SystemExit("Unable to connect to host "
                         "with supplied credentials.")
    return si

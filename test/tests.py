import unittest

import MB_SMF.TMGIServiceAPI as TMGIServiceAPI
import MB_SMF.MBSSessionServiceAPI as MBSSessionServiceAPI

# group tests in suites
tmgi_service = unittest.TestSuite()
tmgi_service.addTests(unittest.defaultTestLoader.loadTestsFromModule(TMGIServiceAPI))

# TODO (borieher): Currently the MBS Session tests are only a placeholder
mbs_session_service = unittest.TestSuite()
mbs_session_service.addTests(unittest.defaultTestLoader.loadTestsFromModule(MBSSessionServiceAPI))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(tmgi_service)
    runner.run(mbs_session_service)

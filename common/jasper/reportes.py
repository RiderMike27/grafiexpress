import inspect
import os

from common.jasper import conector

mypath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/'
MYPATHREPORTES = mypath


def get_report(report, params):

    params = params or {}
    params.update(
        {'SUBREPORT_DIR': MYPATHREPORTES}
    )
    print(mypath + report)
    return conector.Bridge({"report": mypath + report,
                            "params": params,
                            }).get_result()
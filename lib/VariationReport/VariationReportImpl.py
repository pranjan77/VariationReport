# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
from installed_clients.WorkspaceClient import Workspace as Workspace
from .Utils.htmlreportutils import htmlreportutils
import shutil

#END_HEADER


class VariationReport:
    '''
    Module Name:
    VariationReport

    Module Description:
    A KBase module: VariationReport
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        self.hr = htmlreportutils()
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def run_VariationReport(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of type "VariationReportParams" -> structure:
           parameter "variation_object_id" of String
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_VariationReport

        src = "/kb/module/deps/jbrowse"
        dest = os.path.join(self.shared_folder, "jbrowse")
        destination = shutil.copytree(src, dest)  
   
        print("After copying file:")  
        print(os.listdir(destination))  
   


        print (os.listdir("/kb/module/deps"))
        workspace = params['workspace_name']
        outputdir = "/kb/module/deps/jbrowse"
        output = self.hr.create_html_report(self.callback_url, destination, workspace) 
        #END run_VariationReport

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_VariationReport return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]

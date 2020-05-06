/*
A KBase module: VariationReport
*/

module VariationReport {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    typedef structure {
        string variation_object_id;
    } VariationReportParams;



    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_VariationReport(VariationReportParams params) returns (ReportResults output) authentication required;

};

#!/usr/bin/env python
"""
_UpdateAlgoDatasetAssoc_

MySQL implementation of DBSBuffer.UpdateAlgoDatasetAssoc
"""




from WMCore.Database.DBFormatter import DBFormatter

class UpdateAlgoDatasetAssoc(DBFormatter):
    """
    _UpdateAlgoDatasetAssoc_

    Update the in_dbs column for a particular algo/dataset association.
    """
    sql = """UPDATE dbsbuffer_algo_dataset_assoc SET in_dbs = :in_dbs
               WHERE id = :id"""

    def execute(self, assocID = None, inDBS = None, conn = None,
                transaction = False):
        binds = {"id": assocID, "in_dbs": inDBS}
        result = self.dbi.processData(self.sql, binds, conn = conn,
                                          transaction = transaction)

        return

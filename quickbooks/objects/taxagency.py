from base import QuickbooksManagedObject


class TaxAgency(QuickbooksManagedObject):
    """
    QBO definition: Tax Agency is an entity that is associated with a tax rate and identifies the agency to which that tax rate
    applies, that is, the entity that collects those taxes.
    """

    class_dict = {}

    qbo_object_name = "TaxAgency"

    def __init__(self):
        super(TaxAgency, self).__init__()
        self.DisplayName = ""
        self.TaxTrackedOnSales = True
        self.TaxTrackedOnPurchases = False

    def __unicode__(self):
        return self.DisplayName
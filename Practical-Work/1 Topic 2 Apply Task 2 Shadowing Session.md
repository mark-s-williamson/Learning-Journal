

## Specific use cases and scenarios where automated data quality management tools are employed

    Data Validation Reports: In our data validation reports we use Range validation and we compare Target value vs Source Value
    Data Consistency Reports: In our data consistency reports we use Pattern validation. eg. Customer name should not contain numeric values. We also employ Pattern/Range validation and Compare totals against a threshold.
    Merge Process: As part of our ETL merge process we use Syntax Checking. A variety of checks built in that compare target table with source table and prevent merge. Keeps integrity of production tables intact.
    DM6 Process: In our DM6 process we employ Pattern Recognition. eg we sometimes encounter Free-form keyed dates. Causing foreign key constraints to make the ETL fall over. Pattern recognition changes improper dates to -1.
    Mortgage repossession and sale: If shortfall, then it becomes an unsecured loan. We perform a Standard deviation analysis, generating Alerts when a case is x number of standard deviations above or below mean.
    Data Contraints: We use Validto/From and iscurrent, among other constraints to ensure internal consistency of data in tables.
  

## Benefits and challenges of using these tools:

    Benefits: Flags problems that don’t cause tables to fall over.
    Challenges: Entirely created in-house by user. Not universal. Hence prone to blind spots. Standard template for validation rules for improvement. Used mainly when tables fall over/have problems.

Data Consistency Report

    Benefits:
    Challenges: Doesn’t catch creeping or very gradual faults.

Merge Process:

    Benefits: Consistent and robust.
    Challenges: Content-agnostic.

DM6 Pattern Recognition:

    Benefits: Stops things falling down.
    Challenges: Losing data. Doesn’t report how many -1 changes are being made. Wouldn’t spot a ridiculous date if valid.

Integration with existing data pipelines or workflows:

    SQL Server Integration Services - SSIS - (Simon Exley as contact).

Utilize internal resources like wikis, documentation, and knowledge bases to gather insights on automated data quality management within your organization.

    SQL We have access to an internal Stack Overflow and a Lloyds Copilot for knowledge bases.



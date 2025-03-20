# Outcome 1: Evaluate approaches to collaborating with diverse stakeholders in a way that aligns data-driven initiatives with business objectives.

You can meet this outcome by completing the following:

   ## Identify the key stakeholders (e.g., business leaders, IT, data analysts, end users) who are typically involved in data-driven initiatives in your organization:
     * Data Engineer (Myself or a peer)
     * Jon Crump – Stakeholder Relationship Manager
     * Amy Young – Power BI Developer
     * CFA (Customer Financial Assistance) Team Leads – End Users
     * Data Testers – Usually other data engineers or Power BI developers

 ## Analyze effective strategies and best practices for collaborating with this diverse set of stakeholders to ensure alignment between data-driven projects and your organization’s overarching goals.
        Jon Crump – Weekly updates on active tasks for CFA customers. Useful as a point of contact with end users to manage expectations, confirm requirements, and act as a buffer between developers and end users.
        Amy Young – Regular (daily or at least several times per week) check-ins on progress, timelines, and any issues. Confirms the shape of the data as it is being developed through the ETL and what it will look like when it is ready to be adopted into the end-users’ Power BI dashboard.
        CFA Team Leads – First and last points of contact for the project. They define the data request at day 1, receive an update from the relationship manager at day 5, and confirm acceptance at day 10.

# Document your findings in a stakeholder engagement plan, highlighting key considerations for facilitating communication, managing expectations, and maintaining alignment throughout projects.

## Project Timeline:

* Day 1 – Relationship manager relays any queries or concerns to stakeholders and, if nothing prevents work from beginning, confirms that work has begun.
* Day 1-5 – Data Engineer and Power BI developers maintain regular, unscheduled contact with updates on workflow and timescales, confirming the shape of data as it comes through the ETL and the format for acceptance into the Power BI dashboard.
* Day 5 – Mid-project catchup. Data Engineer and Power BI developers update the relationship manager with progress, any roadblocks, or clarifications needed to requirements and to confirm timescales again. The relationship manager relays this to stakeholders.
* Day 5-10 – Data Engineer, Power BI developers, and testers maintain regular contact through ETL and test the ETL and Dashboard output.
* Day 10 – End Project Meeting. Data Engineer, Power BI developer, and tester update the relationship manager on the finished project, identifying any issues and any learnings for requests going forward. The relationship manager contacts stakeholders and confirms acceptance.

# Outcome 2: Argue how a data-driven culture can be championed within an organization by leveraging the synergies between Agile, Lean, and Six Sigma approaches.

You can meet this outcome by completing the following:
## Proposal – Moving from Waterfall to Agile Workflow in CFA MI Projects

  Currently, there is a top-down waterfall strategy for implementing new data products for end users.<br/>
  A dashboard is designated as required, and a detailed requirements gathering exercise is done by Business Analysts, which is passed on to Data Engineers to develop the ETL and then Power BI developers to produce the dashboard.<br/>
  The duration from identifying a need to producing a product can take months, even up to a year for more complex requests. During that time, progress is opaque to the end user, and requirements may change.<br/>

### Transitioning to Agile

  Securing buy-in from the CFA MI leadership team might be the largest hurdle as it involves structural and responsibility changes within the team.<br/><br/>

  Product Owner and Scrum Master roles need to be created. Teams would need to be trained on Agile methodologies, ceremonies, and structures.<br/><br/>

  Key benefits of Agile include:
       * Higher success rate on projects compared to Waterfall
       * Ability to quickly accommodate changes
       * Shorter development cycles
       * Regular stakeholder feedback
       * Easier handling of data complexity

    
  The Product Owner will liaise with a Scrum Master to group the backlog of Jira tasks into a cohesive and achievable epic and then prioritize them with feedback from the end user into sprints.<br/>

   Sprints will be two-week cycles, following the standard Agile model:<br/>

  Sprint Planning → Daily Standups → Sprint Review → Sprint Retrospective → Sprint Planning (continues).<br/>

  Lean and Six Sigma reviews of specific sprints will occur in each Sprint Retrospective, identifying:<br/>
       * Waste (Lean)
       * Variability and defects (Six Sigma)
       * Non-value-added tasks
       * Work that was challenged
       * Data quality issues highlighted in testing or by stakeholders

### Key Performance Indicators (KPIs)

  Stakeholder Feedback<br/>
  Burn Rate<br/>
  Tasks not resolved in single sprints<br/>
  Backlog volume<br/>

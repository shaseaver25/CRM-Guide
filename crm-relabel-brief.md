# cM CRM — Relabel Brief (nonprofit → small business)

**Instance:** crm.stonearch.ai
**Goal:** Reframe the CRM from nonprofit/fundraising language to small-business language, keeping a light **Grants** thread. UI copy + nav only unless a prompt says otherwise — no logic, data, route, or calculation changes.
**How to use:** Hand any block below to the build thread. Each is scoped to one page/area. Statuses reflect what's confirmed applied vs. still open as of this writing.

---

## Terminology mapping (apply everywhere)

| CRM shows (nonprofit) | Use instead (small business) |
|---|---|
| Constituents / Members / Donors | **Customers** (see open decision on Members vs Customers) |
| Donor Accounts | **Clients** |
| Gift Pipeline | **Sales Pipeline** |
| Donor Acquisition Cost (DAC) | **Customer Acquisition Cost (CAC)** |
| Gift / Donation | **Sale / Payment** |
| Giving History | **Payment History** |
| Total Giving | **Total Revenue** |
| Pledge | **Commitment** |
| Major Gift | **Major Deal** |
| Average Gift Size | **Average Deal Size** |
| LYBUNT | **Lapsed Customers** |
| Household | **Company** (open decision) |
| Grant / Grants | **keep** (grants stay in scope) |

---

## Open decisions (resolve these; they change wording downstream)

- [x] **People page label** (resolved): **"Members"** everywhere for the people entity (Add Member, Members list, Lapsed Members). Sales Pipeline keeps standard metric names "Customer Lifetime Value" / "Customer Acquisition Cost".
- [ ] **"Create Household":** keep, or rename to **"Create Company"** (recommended for B2B).
- [x] **Givebutter → Stripe** (resolved). Swap the donation integration for Stripe. Copy change is quick; the actual Stripe connection (Connect/API keys, webhooks, payment sync) is a separate engineering task. Touches both the Dashboard card and the Admin → Integrations page.
- [x] **Clients vs Companies** (resolved): separate. **Companies** → promoted to Main nav. **Clients** → renamed **"Member Clients"** and moved to the **Admin** group. They swap groups.
- [ ] **Sites → Companies** wording cleanup (included in Companies prompt below) — confirm you want it.

---

## 1. Sales Pipeline page — STATUS: ✅ applied & verified

Route `/pipeline`. Confirmed live: title area now "Monitor your sales pipeline and program health across your business"; tabs **Sales Pipeline / Programs / Client Engagements**; cards **Customer Lifetime Value**, **Customer Acquisition Cost** ("precise CAC"), **Average Deal Size**, "Active major deals". Left for reference:

```
UI copy only. On /pipeline:
- Subtitle → "Monitor your sales pipeline and program health across your business"
- Tab "Gift Pipeline" → "Sales Pipeline"; "Programming" → "Programs"; keep "Client Engagements"
- "Total Lifetime Value" → "Customer Lifetime Value"
- "Donor Acquisition Cost" → "Customer Acquisition Cost"; "...precise DAC." → "...precise CAC."
- "Average Gift Size" → "Average Deal Size"; "Active major gifts" → "Active major deals"
- "No major gift opportunities in the pipeline" → "No deals in the pipeline"
- "Progression through the major gift pipeline" → "Progression through the sales pipeline"
- "cultivation strategies" → "follow-up strategies"
- Keep "opportunity/opportunities".
```

## 2. Companies page (promote + rename) — STATUS: ⏳ pending

Route `/sites`. Menu item "Companies" currently lives under the **Admin** group; page title is "Organizations".

```
Promote the "Companies" page to the main navigation and simplify its header.
Route: /sites. Nav + text only — do NOT change the board, stages, KPIs, or actions.

1. Nav: move the "Companies" item OUT of the "Admin" group and INTO the "Main" group
   (top level, alongside Dashboard, Members, Contacts, Clients, Sales Pipeline).
   Keep the label "Companies" and its icon.
2. Page title: "Organizations" → "Companies".
3. Remove the subtitle "Schools and organizations we're working with" entirely.
4. Wording cleanup for consistency:
   - "Total Sites"    → "Total Companies"
   - "Add Site"       → "Add Company"
   - "Search sites…"  → "Search companies…"
5. Leave unchanged: the other KPIs (Prospects, In Pipeline, Active Partners),
   the Pipeline/Kanban/List toggle, and the stage columns
   (Prospects, Contacted, In Conversation, Pilot, Active Partners).
```

## 3. Members list — STATUS: ⏳ pending

Route `/constituents`.

```
UI copy only. On /constituents (people label is "Members"):
- Section heading "Constituents" → "Members"
- Subtitle "Manage your donor and constituent database" → "Manage your member database"
- Button "Add Constituent" → "Add Member"
- Filter "LYBUNT Segmentation" → "Lapsed Members"
- Filter description "Last Year But Unfortunately Not This year (Gave ≥$1.00 last year, $0 this year)"
  → "Bought last year, nothing yet this year"
- Card label "TOTAL LTV" → "LIFETIME VALUE"
- Keep "Clean Emails", "Bulk Import", search placeholder, and nav label "Members".
- NOTE: the people entity is "Member" everywhere. The Sales Pipeline keeps the standard
  metric names "Customer Lifetime Value" / "Customer Acquisition Cost" (conventional terms).
```

## 4. 360° Customer View (modal) — STATUS: ✅ applied & verified

Applied via Lovable (crm4creatempls, commit ad862c3). Decision resolved: **"Create Household" → "Create Company"**. Diff confirmed: title, Giving History → Payment History, Total Giving → Total Revenue, gift(s) recorded → payment(s) recorded, Add Gift → Record Payment, Record Pledge → Record Commitment, Track Major Gift → Track Major Deal, connections line, and all three Create Household strings (trigger button, dialog title, submit button). Left unchanged (out of scope, as directed): CreateHouseholdDialog's description text ("Group constituents into a household...") and Grants/Quick Actions/Relationships/Tasks items.

```
UI copy only. On the customer detail modal:
- Title "360° Constituent View" → "360° Customer View"
- "Giving History" → "Payment History"
- "Total Giving" → "Total Revenue"
- "0 gifts recorded" / "No gifts recorded yet" / "Record First Gift"
  → "0 payments recorded" / "No payments recorded yet" / "Record First Payment"
- "Add Gift" → "Record Payment"
- "Record Pledge" → "Record Commitment"
- "Track Major Gift" → "Track Major Deal"
- "...connections to other constituents." → "...to other customers."
- KEEP (in scope): "Linked Grant Opportunities", "Link Grant", "No linked grants yet", "Link First Grant".
- KEEP: "Quick Actions", "Log Interaction", "Contact Information", "Send Email",
  "Relationships", "Add Relationship", "Related Tasks", "Create Task".
- "Create Household" → "Create Company" (resolved).
```

## 5. Dashboard — STATUS: ⏳ pending

Route `/`.

```
UI copy only. On the Dashboard:
- Recent Activity "New constituent added" → "New customer added"
- Keep quick actions, "My Tasks", "cM Customers", "Manage Customers",
  "Upcoming Events", "Create Event".
- Replace the Givebutter card with a Stripe card:
    - Title "Givebutter" → "Stripe"
    - Body "Connect Givebutter to sync donations and recurring plans"
      → "Connect Stripe to sync payments and subscriptions"
    - Keep the "Connect" button.
  NOTE: this is copy only. Wiring the real Stripe integration (Stripe Connect / API keys /
  webhooks / payment sync) is a separate engineering task — see prompt 9 below.
```

## 6. Member Clients page (rename + relocate) — STATUS: ⏳ pending

Route `/admin/customers`. Resolved: rename "Clients" → **"Member Clients"** and move it from the Main nav group DOWN into the **Admin** group.

```
Rename and relocate the "Clients" page. Route /admin/customers. Nav + copy only —
do not change table logic, data, or account-provisioning behavior.

1. Nav: move the "Clients" item OUT of the "Main" group and INTO the "Admin" group
   (with Integrations, Admin, Escalations, Support Log). Rename the label "Clients"
   → "Member Clients".  (Companies moves the opposite way — Admin → Main, per prompt 2.)
2. Page title "Stone Arch Clients" → "Member Clients".
3. Subtitle "Manage client accounts and relationships" → "Manage member client accounts and CRM setup".
4. Button "Add Client" → "Add Member Client".
5. KPI "Total Customers" → "Total Member Clients".
6. Keep "Active", "Pending Setup", "Past Due" and the table columns
   (Name, Type, Tier, Status, Contact, Users, Last Sync).
```

## 7. Content Repository — STATUS: ⏳ pending

Route `/content-repository`.

```
UI copy only:
- Subtitle "Reusable content for grant proposals" → "Reusable content for proposals and grant applications"
- Keep everything else (grants stay in scope).
```

## 8. Global / app-wide — STATUS: ⏳ pending

```
UI copy only, app-wide:
- Browser tab / app title "cM CRM - Fundraising Management System"
  → "cM CRM - Customer Management System"
- Left-nav Main group should read: Dashboard, Members, Contacts, Sales Pipeline, Companies.
  (Clients moves OUT of Main into the Admin group — see prompt 6.)
- Admin group should read: Member Clients, Integrations, Admin, Escalations, Support Log.
- If any items still show Constituents / Donor Accounts / Grants / Donations / Major Gifts /
  Pledges in the MAIN group, revert to the list above.
- Note: there is a duplicate "Major Gifts" entry appearing in some nav states — remove the dupe.
```

## 9. Stripe integration (replaces Givebutter) — STATUS: ⏳ pending / engineering task

Two parts: (a) copy swap on the Dashboard card + Admin → Integrations page, (b) the real integration build. Part (a) can ship now; part (b) is a scoped engineering task.

```
Part A — copy only (ship now):
- Dashboard card: "Givebutter" → "Stripe"; body → "Connect Stripe to sync payments and
  subscriptions"; keep "Connect".
- Admin → Integrations page: replace any "Givebutter" entry/label with "Stripe" and update
  its description to reference payments/subscriptions instead of donations/recurring plans.

Part B — integration build (separate task, do NOT fake in copy):
- Implement Stripe connection (Stripe Connect or API keys), store credentials securely,
  handle OAuth/connect flow from the "Connect" button.
- Sync Stripe payments → the customer's Payment History (formerly Giving History) and the
  Customer Lifetime Value / Total Revenue fields.
- Sync Stripe subscriptions → recurring "Commitments".
- Add webhook handling for payment succeeded / refunded / subscription updated.
- Confirm which product handles this today (QuickBooks/Stripe connectors exist in the stack).
```

---

## Known bugs spotted (not relabeling — flag to build thread)

- Duplicate **"Major Gifts"** menu item appears in some nav states.
- Nav intermittently reverts to nonprofit labels while a page is still loading — confirm the label set is coming from one source of truth, not per-page.

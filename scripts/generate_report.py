"""
Script to generate the comprehensive academic and industry final project report for:
Design and Implementation of a Wazuh-Based SOC Home Lab for Attack Detection and Log Analysis
Author: Natto Muni Chakma
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            # Skip cover page
            return

        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))

        # Header
        self.drawString(54, 11 * 72 - 36, "Design and Implementation of a Wazuh-Based SOC Home Lab")
        self.drawRightString(8.5 * 72 - 54, 11 * 72 - 36, "Final Project Report | Capstone")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.75)
        self.line(54, 11 * 72 - 42, 8.5 * 72 - 54, 11 * 72 - 42)

        # Footer
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.75)
        self.line(54, 48, 8.5 * 72 - 54, 48)
        self.drawString(54, 34, "Author: Natto Muni Chakma | Andhra University College of Engineering")
        self.drawRightString(8.5 * 72 - 54, 34, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()


def build_pdf(filename="reports/Final_Report.pdf"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    primary_color = colors.HexColor("#0F172A")    # Slate 900
    accent_color = colors.HexColor("#0284C7")     # Sky 600
    secondary_color = colors.HexColor("#334155")  # Slate 700
    dark_blue = colors.HexColor("#1E3A8A")        # Blue 900
    bg_light = colors.HexColor("#F8FAFC")         # Slate 50
    border_color = colors.HexColor("#CBD5E1")     # Slate 300

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=30,
        textColor=dark_blue,
        alignment=1, # Center
        spaceAfter=15
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=secondary_color,
        alignment=1,
        spaceAfter=25
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=dark_blue,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=accent_color,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=primary_color,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=3
    )

    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#0F172A")
    )

    callout_style = ParagraphStyle(
        'Callout_Text',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor("#1E293B")
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=primary_color
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    story = []

    # ==========================================
    # COVER PAGE
    # ==========================================
    story.append(Spacer(1, 40))
    story.append(Paragraph("SECURITY OPERATIONS CENTER (SOC) CAPSTONE PROJECT", ParagraphStyle('SubHeader', fontName='Helvetica-Bold', fontSize=10, textColor=accent_color, alignment=1, spaceAfter=15)))
    story.append(Paragraph("Design and Implementation of a Wazuh-Based SOC Home Lab for Attack Detection and Log Analysis", title_style))
    story.append(Paragraph("A Comprehensive Technical Investigation into Endpoint Telemetry, eBPF Kernel Monitoring, Multi-Vector Cyber Attack Detection, and SIEM Alert Correlation", subtitle_style))
    story.append(HRFlowable(width="60%", thickness=2, color=accent_color, spaceBefore=10, spaceAfter=30))

    meta_data = [
        [Paragraph("<b>Author / Researcher:</b>", body_style), Paragraph("Natto Muni Chakma", body_style)],
        [Paragraph("<b>Degree Program:</b>", body_style), Paragraph("B.Tech in Computer Science and Engineering", body_style)],
        [Paragraph("<b>Institution:</b>", body_style), Paragraph("Andhra University College of Engineering", body_style)],
        [Paragraph("<b>Domain Specialization:</b>", body_style), Paragraph("Cybersecurity, SIEM, SOC Operations, Threat Detection", body_style)],
        [Paragraph("<b>Core Technologies:</b>", body_style), Paragraph("Wazuh 4.x, Microsoft Sysmon (Win/Linux), VirtualBox, Kali Linux", body_style)],
        [Paragraph("<b>Repository:</b>", body_style), Paragraph("https://github.com/NATTOMR/Design-and-Implementation-of-a-Wazuh-Based-SOC-Home-Lab-for-Attack-Detection-and-Log-Analysis", body_style)],
        [Paragraph("<b>Date of Submission:</b>", body_style), Paragraph("August 2026", body_style)]
    ]
    t_meta = Table(meta_data, colWidths=[160, 320])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg_light),
        ('BOX', (0,0), (-1,-1), 1, border_color),
        ('INNERGRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_meta)

    story.append(Spacer(1, 40))
    abstract_box = [
        [Paragraph("<b>EXECUTIVE ABSTRACT:</b> This research report details the architectural design, deployment, and validation of an enterprise-grade Security Operations Center (SOC) home laboratory. Built entirely on open-source and standard enterprise security platforms—primarily the Wazuh SIEM ecosystem integrated with Microsoft Sysmon on Windows and eBPF-based Sysmon for Linux—this project proves end-to-end detection engineering. Multiple cyberattack scenarios (network reconnaissance, SSH/RDP brute-force, unauthorized PowerShell execution, and persistence techniques) were simulated via Kali Linux and detected in real-time, resulting in over 11,000+ telemetry events and actionable alerts mapped against the MITRE ATT&CK framework.", callout_style)]
    ]
    t_abs = Table(abstract_box, colWidths=[500])
    t_abs.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#94A3B8")),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t_abs)

    story.append(PageBreak())

    # ==========================================
    # CHAPTER 1: INTRODUCTION & PROJECT SCOPE
    # ==========================================
    story.append(Paragraph("1. Introduction & Project Scope", h1_style))
    story.append(Paragraph("Modern enterprise cyber defense relies heavily on Security Information and Event Management (SIEM) solutions coupled with Security Operations Center (SOC) workflows. As cyber threats increase in stealth and sophistication, traditional signature-based antiviruses fail to provide sufficient visibility into advanced threat actor behavior, fileless attacks, and lateral movement.", body_style))
    story.append(Paragraph("The primary aim of this capstone project is to engineer an enterprise-grade, cost-effective SOC Home Lab. By deploying Wazuh as the centralized SIEM/XDR platform alongside deep kernel telemetry collectors (Microsoft Sysmon and Sysmon for Linux), this lab bridges theoretical cybersecurity knowledge with practical offensive and defensive capabilities.", body_style))

    story.append(Paragraph("Key Objectives", h2_style))
    story.append(Paragraph("• <b>Architecture Design:</b> Establish an isolated, multi-node virtual network using Oracle VirtualBox NAT Networking.", bullet_style))
    story.append(Paragraph("• <b>SIEM & XDR Deployment:</b> Install, configure, and harden Ubuntu Server 24.04 hosting Wazuh Manager, Wazuh Indexer (OpenSearch), and Wazuh Dashboard.", bullet_style))
    story.append(Paragraph("• <b>Endpoint Telemetry Integration:</b> Deploy Wazuh Agents with Microsoft Sysmon on Windows 11 and eBPF-driven Sysmon for Linux.", bullet_style))
    story.append(Paragraph("• <b>Offensive Attack Simulation:</b> Execute realistic multi-stage cyber attacks from a Kali Linux adversary node.", bullet_style))
    story.append(Paragraph("• <b>Detection Engineering:</b> Author custom decoders and XML rules, validating detection triggers against MITRE ATT&CK tactics.", bullet_style))

    story.append(Spacer(1, 10))

    # ==========================================
    # CHAPTER 2: LAB ARCHITECTURE & ENVIRONMENT SPECIFICATIONS
    # ==========================================
    story.append(Paragraph("2. Lab Architecture & Node Specifications", h1_style))
    story.append(Paragraph("The lab is structured inside an isolated VirtualBox NAT Network (10.0.2.0/24 subnet), preventing accidental external network leakage while enabling unrestricted inter-node communication for realistic attack traffic and encrypted log forwarding.", body_style))

    vm_specs = [
        [Paragraph("Node / Hostname", table_header), Paragraph("Operating System", table_header), Paragraph("Role in SOC Lab", table_header), Paragraph("Assigned IP", table_header), Paragraph("Resources", table_header)],
        [Paragraph("<b>Wazuh Server</b>", table_cell), Paragraph("Ubuntu Server 24.04 LTS", table_cell), Paragraph("SIEM Manager, Indexer & Dashboard", table_cell), Paragraph("10.0.2.15", table_cell), Paragraph("4 GB RAM, 2 vCPU, 50 GB Disk", table_cell)],
        [Paragraph("<b>Victim Endpoint</b>", table_cell), Paragraph("Windows 11 Pro (64-bit)", table_cell), Paragraph("Primary Monitored Workstation", table_cell), Paragraph("10.0.2.20 / DHCP", table_cell), Paragraph("4 GB RAM, 2 vCPU, 60 GB Disk", table_cell)],
        [Paragraph("<b>Attacker Node</b>", table_cell), Paragraph("Kali Linux (Rolling)", table_cell), Paragraph("Offensive Attack & Recon Simulation", table_cell), Paragraph("10.0.2.30 / DHCP", table_cell), Paragraph("2 GB RAM, 2 vCPU, 30 GB Disk", table_cell)],
        [Paragraph("<b>Host Machine</b>", table_cell), Paragraph("Windows 11 Pro (Physical)", table_cell), Paragraph("Hypervisor Host (Oracle VirtualBox)", table_cell), Paragraph("Host Gateway", table_cell), Paragraph("16 GB RAM, Intel Core", table_cell)]
    ]
    t_vm = Table(vm_specs, colWidths=[90, 110, 140, 75, 85])
    t_vm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), dark_blue),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [bg_light, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_vm)

    story.append(Spacer(1, 10))

    # ==========================================
    # CHAPTER 3: WAZUH SIEM PLATFORM DEPLOYMENT
    # ==========================================
    story.append(Paragraph("3. Wazuh SIEM Platform Deployment & Services", h1_style))
    story.append(Paragraph("Wazuh operates as an all-in-one centralized architecture comprising three critical microservices:", body_style))
    story.append(Paragraph("1. <b>Wazuh Manager:</b> Receives encrypted telemetry from agent daemons on TCP port 1514, handles agent registration on port 1515, executes real-time decoder matching, and processes the correlation rule engine.", body_style))
    story.append(Paragraph("2. <b>Wazuh Indexer:</b> A high-performance, distributed OpenSearch engine providing scalable document indexing, document storage, and multi-field querying across millions of security events.", body_style))
    story.append(Paragraph("3. <b>Wazuh Dashboard:</b> A rich React-based web user interface operating over HTTPS (port 443) that provides interactive visual analytics, threat hunting panels, and compliance reporting.", body_style))

    story.append(Paragraph("Service Verification & Health Checks", h2_style))
    story.append(Paragraph("Following deployment, all system daemons were verified using standard systemd utilities, confirming zero runtime errors across `wazuh-manager`, `wazuh-indexer`, and `wazuh-dashboard`.", body_style))

    story.append(PageBreak())

    # ==========================================
    # CHAPTER 4: ENDPOINT TELEMETRY & SYSMON INTEGRATION
    # ==========================================
    story.append(Paragraph("4. Endpoint Telemetry & Sysmon Integration (Windows & Linux)", h1_style))
    story.append(Paragraph("Default operating system event logging often fails to record critical process lineage, command-line arguments, and socket-to-process bindings. To bridge this visibility gap, Microsoft Sysmon was deployed across both Windows and Linux endpoints.", body_style))

    story.append(Paragraph("Windows 11 Sysmon Architecture", h2_style))
    story.append(Paragraph("Sysmon operates as a Windows system service and device driver that remains resident across system boots. The Wazuh Agent configuration (`ossec.conf`) was updated to subscribe directly to the `Microsoft-Windows-Sysmon/Operational` event channel using the native Windows Event Log API.", body_style))

    story.append(Paragraph("Sysmon for Linux (eBPF) Architecture", h2_style))
    story.append(Paragraph("On Linux endpoints, `sysmonforlinux` utilizes extended Berkeley Packet Filter (eBPF) programs injected into kernel tracepoints. This enables non-intrusive, microsecond-latency capture of process lifecycle events and socket connections without requiring kernel modifications. Sysmon events stream directly into `/var/log/syslog` and are ingested by the Linux Wazuh Agent.", body_style))

    sysmon_events = [
        [Paragraph("Event ID", table_header), Paragraph("Event Name", table_header), Paragraph("Platform", table_header), Paragraph("Operational SOC Value & Detection Coverage", table_header)],
        [Paragraph("<b>1</b>", table_cell), Paragraph("Process Creation", table_cell), Paragraph("Win & Linux", table_cell), Paragraph("Captures full CLI arguments, ParentProcessId, ProcessGuid, hashes, user context.", table_cell)],
        [Paragraph("<b>3</b>", table_cell), Paragraph("Network Connection", table_cell), Paragraph("Win & Linux", table_cell), Paragraph("Identifies socket bindings, destination IPs, ports, and initiating binary.", table_cell)],
        [Paragraph("<b>5</b>", table_cell), Paragraph("Process Terminated", table_cell), Paragraph("Win & Linux", table_cell), Paragraph("Monitors process lifecycle and malware termination behavior.", table_cell)],
        [Paragraph("<b>9</b>", table_cell), Paragraph("Raw Access Read", table_cell), Paragraph("Linux", table_cell), Paragraph("Detects direct device access (`/dev/sda`, memory scraping, credential dumps).", table_cell)],
        [Paragraph("<b>11</b>", table_cell), Paragraph("File Create", table_cell), Paragraph("Win & Linux", table_cell), Paragraph("Detects dropped malware payloads in `/tmp/`, `C:\\Windows\\Temp`, startup folders.", table_cell)],
        [Paragraph("<b>12/13</b>", table_cell), Paragraph("Registry Events", table_cell), Paragraph("Windows", table_cell), Paragraph("Monitors Run/RunOnce persistence keys and security policy tampering.", table_cell)],
        [Paragraph("<b>23</b>", table_cell), Paragraph("File Delete", table_cell), Paragraph("Win & Linux", table_cell), Paragraph("Tracks anti-forensic log wiping, ransomware file replacements.", table_cell)]
    ]
    t_sysmon = Table(sysmon_events, colWidths=[45, 105, 70, 280])
    t_sysmon.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), dark_blue),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [bg_light, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_sysmon)

    story.append(Spacer(1, 10))

    # ==========================================
    # CHAPTER 5: OFFENSIVE ATTACK SIMULATIONS
    # ==========================================
    story.append(Paragraph("5. Offensive Attack Simulations & Threat Scenarios", h1_style))
    story.append(Paragraph("To rigorously validate the detection pipeline, multiple offensive security exercises were launched against the lab nodes using Kali Linux:", body_style))

    attacks_data = [
        [Paragraph("Scenario #", table_header), Paragraph("Attack Technique", table_header), Paragraph("Tool / Command", table_header), Paragraph("Target Node", table_header), Paragraph("Observed Wazuh Detection", table_header)],
        [Paragraph("<b>AS-01</b>", table_cell), Paragraph("Host Discovery & TCP Port Scan", table_cell), Paragraph("`nmap -sS -sV -O 10.0.2.20`", table_cell), Paragraph("Windows 11", table_cell), Paragraph("Nmap SYN scan alert & multi-port connection spike", table_cell)],
        [Paragraph("<b>AS-02</b>", table_cell), Paragraph("RDP Authentication Brute Force", table_cell), Paragraph("`hydra -l admin -P wordlist rdp://`", table_cell), Paragraph("Windows 11", table_cell), Paragraph("Windows Event 4625 (Rule 18152: Logon Failure Threshold)", table_cell)],
        [Paragraph("<b>AS-03</b>", table_cell), Paragraph("Suspicious PowerShell CLI Execution", table_cell), Paragraph("`powershell -enc ... -ExecutionPolicy Bypass`", table_cell), Paragraph("Windows 11", table_cell), Paragraph("Sysmon Event 1 & Custom Rule for Encoded PowerShell", table_cell)],
        [Paragraph("<b>AS-04</b>", table_cell), Paragraph("Linux Sudo & Privilege Escalation", table_cell), Paragraph("`sudo su` & unauthorized user switches", table_cell), Paragraph("Kali / Linux", table_cell), Paragraph("Rule 5502: PAM Login session closed / authentication alert", table_cell)],
        [Paragraph("<b>AS-05</b>", table_cell), Paragraph("C2 Network Beacon Simulation", table_cell), Paragraph("`nc -zv 10.0.2.15 4444` / egress tests", table_cell), Paragraph("Linux Host", table_cell), Paragraph("Sysmon Event 3 & Process Terminate Event 5 ingestion", table_cell)]
    ]
    t_attacks = Table(attacks_data, colWidths=[50, 110, 125, 75, 140])
    t_attacks.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), dark_blue),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [bg_light, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_attacks)

    story.append(PageBreak())

    # ==========================================
    # CHAPTER 6: DETECTION ENGINEERING & MITRE ATT&CK
    # ==========================================
    story.append(Paragraph("6. Detection Engineering & MITRE ATT&CK Mapping", h1_style))
    story.append(Paragraph("Wazuh utilizes an XML-based ruleset architecture featuring over 3,000 built-in rules organized into severity levels ranging from Level 0 (Ignored) to Level 15 (Critical Alert).", body_style))

    story.append(Paragraph("Custom Detection Rules Implemented (`local_rules.xml`)", h2_style))
    story.append(Paragraph("To augment built-in coverage, specialized local rules were authored to detect advanced adversarial tactics:", body_style))

    rule_code = """<group name="custom_rules,sysmon,threat_hunting">
  <!-- Rule 100002: Encoded or Suspicious PowerShell Execution -->
  <rule id="100002" level="10">
    <if_group>sysmon_process_create</if_group>
    <field name="win.eventdata.commandLine" type="pcre2">(?i)-enc|-encodedcommand|-exec.*bypass</field>
    <description>Suspicious Encoded PowerShell Execution Detected on Endpoint</description>
    <mitre><id>T1059.001</id></mitre>
  </rule>

  <!-- Rule 100003: Multiple Failed Logons / RDP Brute Force -->
  <rule id="100003" level="12" frequency="5" timeframe="60">
    <if_matched_sid>18152</if_matched_sid>
    <same_source_ip />
    <description>Potential RDP / Windows Brute Force Attack in Progress</description>
    <mitre><id>T1110.001</id></mitre>
  </rule>
</group>"""

    t_code = Table([[Paragraph(rule_code.replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>"), code_style)]], colWidths=[500])
    t_code.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0F172A")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#334155")),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_code)

    story.append(Paragraph("MITRE ATT&CK Framework Alignment", h2_style))
    story.append(Paragraph("• <b>Reconnaissance (T1595):</b> Active scanning and port discovery detected via network connection frequency.", bullet_style))
    story.append(Paragraph("• <b>Initial Access / Credential Access (T1110):</b> Password brute-force detected via Event 4625 rate analysis.", bullet_style))
    story.append(Paragraph("• <b>Execution (T1059.001):</b> Command and Scripting Interpreter (PowerShell, bash, dash) captured by Sysmon Event ID 1.", bullet_style))
    story.append(Paragraph("• <b>Persistence (T1547):</b> Boot or Logon Autostart Execution monitored via Windows Registry key monitoring.", bullet_style))
    story.append(Paragraph("• <b>Defense Evasion (T1070):</b> Indicator Removal / File Deletion captured via Sysmon Event ID 23.", bullet_style))

    story.append(Spacer(1, 10))

    # ==========================================
    # CHAPTER 7: THREAT HUNTING, INGESTION METRICS & RESULTS
    # ==========================================
    story.append(Paragraph("7. Ingestion Metrics, Threat Hunting & Analytical Results", h1_style))
    story.append(Paragraph("During the evaluation window, the SOC Home Lab processed intensive event streams across Windows and Linux nodes, confirming high-throughput reliability without ingestion drops:", body_style))

    metrics_data = [
        [Paragraph("Telemetry Source", table_header), Paragraph("Agent Node", table_header), Paragraph("Total Events Ingested", table_header), Paragraph("Key Ingested Types", table_header), Paragraph("Alert Severity Levels", table_header)],
        [Paragraph("<b>Sysmon for Linux (eBPF)</b>", table_cell), Paragraph("Kali Linux (004)", table_cell), Paragraph("<b>10,135+ Hits</b>", table_cell), Paragraph("Event ID 5, Event ID 1, Event ID 3", table_cell), Paragraph("Level 3 to Level 10", table_cell)],
        [Paragraph("<b>Windows Sysmon & Events</b>", table_cell), Paragraph("Windows 11 (003)", table_cell), Paragraph("<b>1,427+ Hits</b>", table_cell), Paragraph("Event ID 1, 3, 4625, Registry, FIM", table_cell), Paragraph("Level 3 to Level 12", table_cell)],
        [Paragraph("<b>Linux System & PAM Logs</b>", table_cell), Paragraph("Ubuntu / Kali", table_cell), Paragraph("<b>1,044+ Hits</b>", table_cell), Paragraph("Rule 5502, sudo sessions, sshd logs", table_cell), Paragraph("Level 3 to Level 7", table_cell)],
        [Paragraph("<b>Total Lab Ingestion</b>", table_cell), Paragraph("All Multi-Nodes", table_cell), Paragraph("<b>12,600+ Events</b>", table_cell), Paragraph("Cross-platform telemetry correlation", table_cell), Paragraph("Unified SIEM Dashboard", table_cell)]
    ]
    t_metrics = Table(metrics_data, colWidths=[110, 85, 95, 120, 90])
    t_metrics.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), dark_blue),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [bg_light, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_metrics)

    story.append(PageBreak())

    # ==========================================
    # CHAPTER 8: OPERATIONAL TROUBLESHOOTING & HARDENING
    # ==========================================
    story.append(Paragraph("8. Operational Troubleshooting & Hardening", h1_style))
    story.append(Paragraph("Real-world SOC deployments inevitably encounter communication roadblocks, agent disconnections, and parser bottlenecks. Key resolutions discovered during implementation include:", body_style))

    story.append(Paragraph("• <b>Agent Connectivity (Port 1514/1515):</b> Ensured Ubuntu UFW firewall explicitly permitted TCP traffic for ports 1514 and 1515. Resolved NAT gateway routing issues using consistent VirtualBox DHCP leases.", bullet_style))
    story.append(Paragraph("• <b>Sysmon Event Channel Ingestion:</b> Verified Windows Agent subscription to `Microsoft-Windows-Sysmon/Operational` using `eventchannel` log format in `ossec.conf`.", bullet_style))
    story.append(Paragraph("• <b>Sysmon for Linux Kernel Dependencies:</b> Ensured Linux hosts satisfied minimum eBPF kernel requirements (>= 5.4) and verified BPF virtual filesystem mounting via `mount | grep bpf`.", bullet_style))
    story.append(Paragraph("• <b>Service Resiliency & Health Checks:</b> Established standardized PowerShell and bash recovery scripts (`NET START WazuhSvc`, `systemctl restart wazuh-manager`) to ensure rapid service recovery.", bullet_style))

    story.append(Spacer(1, 10))

    # ==========================================
    # CHAPTER 9: CONCLUSION & FUTURE WORK
    # ==========================================
    story.append(Paragraph("9. Conclusion & Future Roadmap", h1_style))
    story.append(Paragraph("This project successfully demonstrated the design, deployment, and practical operation of a comprehensive Wazuh-based SOC Home Lab. By unifying multi-platform endpoint telemetry (Windows Sysmon and Linux eBPF) into a centralized SIEM, the lab provides end-to-end visibility into host-level process creation, network activity, credential attacks, and unauthorized system modifications.", body_style))

    story.append(Paragraph("Future SOC Enhancements Roadmap", h2_style))
    story.append(Paragraph("• <b>Network Intrusion Detection System (NIDS):</b> Integrate Suricata to capture full network packet payload inspection and signature-based exploit detection.", bullet_style))
    story.append(Paragraph("• <b>Threat Intelligence & Enrichment:</b> Connect VirusTotal, AbuseIPDB, and AlienVault OTX APIs into Wazuh integration pipelines for automated IoC scoring.", bullet_style))
    story.append(Paragraph("• <b>Security Orchestration, Automation, and Response (SOAR):</b> Deploy Shuffle SOAR to automate active response actions (e.g. automated host isolation upon high-severity alert triggers).", bullet_style))
    story.append(Paragraph("• <b>Incident Management:</b> Integrate TheHive and MISP for structured incident ticketing and threat intelligence sharing.", bullet_style))

    story.append(Spacer(1, 15))

    # Sign-off block
    story.append(HRFlowable(width="100%", thickness=1, color=border_color, spaceBefore=10, spaceAfter=15))
    story.append(Paragraph("<b>Report Authorization & Acknowledgement:</b><br/>"
                           "This report certifies the successful execution, empirical testing, and academic fulfillment of the SOC Home Lab capstone project.<br/>"
                           "<b>Author:</b> Natto Muni Chakma &nbsp;|&nbsp; <b>Institution:</b> Andhra University College of Engineering &nbsp;|&nbsp; <b>Status:</b> Approved & Completed", callout_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Report generated successfully at: {filename}")

if __name__ == "__main__":
    build_pdf()

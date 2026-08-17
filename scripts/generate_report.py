"""
Academic & Enterprise Project Report Generator
Project: Design and Implementation of a Wazuh-Based SOC Home Lab for Attack Detection and Log Analysis
Author: Natto Muni Chakma
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Image
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
            # Decorative cover page border
            self.saveState()
            self.setStrokeColor(colors.HexColor("#0284C7"))
            self.setLineWidth(4)
            self.rect(24, 24, 8.5 * 72 - 48, 11 * 72 - 48)
            self.setStrokeColor(colors.HexColor("#0F172A"))
            self.setLineWidth(1)
            self.rect(28, 28, 8.5 * 72 - 56, 11 * 72 - 56)
            self.restoreState()
            return

        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#0F172A"))

        # Header
        self.drawString(54, 11 * 72 - 36, "Wazuh SOC Home Lab: Attack Detection & Log Analysis")
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawRightString(8.5 * 72 - 54, 11 * 72 - 36, "Comprehensive Technical & Academic Report")
        
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(54, 11 * 72 - 42, 8.5 * 72 - 54, 11 * 72 - 42)

        # Footer
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(54, 45, 8.5 * 72 - 54, 45)
        
        self.drawString(54, 32, "Author: Natto Muni Chakma | Andhra University College of Engineering")
        self.drawRightString(8.5 * 72 - 54, 32, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()


def create_code_box(code_text, code_style):
    formatted = code_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>").replace(" ", "&nbsp;")
    p = Paragraph(formatted, code_style)
    t = Table([[p]], colWidths=[504])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('LINELEFT', (0,0), (-1,-1), 3.5, colors.HexColor("#0284C7")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    return t

def create_image_box(image_path, caption_text, width=500, height=230, caption_style=None):
    story_elements = []
    if os.path.exists(image_path):
        img = Image(image_path, width=width, height=height)
        t_img = Table([[img]], colWidths=[width])
        t_img.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#94A3B8")),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ]))
        story_elements.append(t_img)
        if caption_style:
            story_elements.append(Spacer(1, 3))
            story_elements.append(Paragraph(f"<b>Figure:</b> <i>{caption_text}</i>", caption_style))
        story_elements.append(Spacer(1, 8))
    return story_elements


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

    # Palette
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
        fontSize=21,
        leading=26,
        textColor=dark_blue,
        alignment=1,
        spaceAfter=12
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=secondary_color,
        alignment=1,
        spaceAfter=20
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13.5,
        leading=17,
        textColor=dark_blue,
        spaceBefore=14,
        spaceAfter=5,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=accent_color,
        spaceBefore=9,
        spaceAfter=3,
        keepWithNext=True
    )

    h3_style = ParagraphStyle(
        'Heading3_Custom',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12.5,
        textColor=secondary_color,
        spaceBefore=7,
        spaceAfter=2,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=primary_color,
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=body_style,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2.5
    )

    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#0F172A")
    )

    caption_style = ParagraphStyle(
        'Caption_Style',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#475569"),
        alignment=1
    )

    callout_style = ParagraphStyle(
        'Callout_Text',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1E293B")
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=primary_color
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=primary_color
    )

    table_cell_code = ParagraphStyle(
        'TableCellCode',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#0F172A")
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.white
    )

    story = []

    # =========================================================================
    # 1. COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 25))
    story.append(Paragraph("SECURITY OPERATIONS CENTER (SOC) RESEARCH REPORT", ParagraphStyle('SubHeader', fontName='Helvetica-Bold', fontSize=10, textColor=accent_color, alignment=1, spaceAfter=10)))
    story.append(Paragraph("Design and Implementation of a Wazuh-Based SOC Home Lab for Attack Detection and Log Analysis", title_style))
    story.append(Paragraph("Comprehensive Technical Investigation into Multi-Platform Telemetry, eBPF Kernel Monitoring, Cyber Attack Detection Engineering, and SIEM Log Analysis", subtitle_style))
    story.append(HRFlowable(width="70%", thickness=2, color=accent_color, spaceBefore=5, spaceAfter=20))

    meta_data = [
        [Paragraph("<b>Author & Researcher:</b>", body_style), Paragraph("Natto Muni Chakma", body_style)],
        [Paragraph("<b>Academic Department:</b>", body_style), Paragraph("Computer Science and Engineering", body_style)],
        [Paragraph("<b>Institution:</b>", body_style), Paragraph("Andhra University College of Engineering", body_style)],
        [Paragraph("<b>Specialization:</b>", body_style), Paragraph("Cybersecurity, SOC Operations, SIEM Architecture, Threat Hunting", body_style)],
        [Paragraph("<b>Platform Stack:</b>", body_style), Paragraph("Wazuh 4.x (Manager/Indexer/Dashboard), Microsoft Sysmon (Windows & Linux eBPF)", body_style)],
        [Paragraph("<b>Virtualization:</b>", body_style), Paragraph("Oracle VirtualBox Isolated NAT Network (10.0.2.0/24 Subnet)", body_style)],
        [Paragraph("<b>Repository URL:</b>", body_style), Paragraph("https://github.com/NATTOMR/Design-and-Implementation-of-a-Wazuh-Based-SOC-Home-Lab-for-Attack-Detection-and-Log-Analysis", body_style)],
        [Paragraph("<b>Date of Publication:</b>", body_style), Paragraph("August 2026", body_style)]
    ]
    t_meta = Table(meta_data, colWidths=[150, 354])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg_light),
        ('BOX', (0,0), (-1,-1), 1, border_color),
        ('INNERGRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_meta)

    story.append(Spacer(1, 20))
    abstract_box = [
        [Paragraph("<b>EXECUTIVE ABSTRACT:</b><br/>"
                   "This capstone report documents the architecture, deployment, offensive validation, and defensive detection engineering of a robust Security Operations Center (SOC) home laboratory. Utilizing the open-source Wazuh SIEM ecosystem integrated with Microsoft Sysmon for Windows and eBPF-driven Sysmon for Linux, this environment achieves comprehensive visibility across host process lifecycles, network sockets, user authentication, and system configurations. Multiple real-world attack vectors (Nmap network reconnaissance, Hydra brute-force authentication, PowerShell execution, and unauthorized privileged commands) were executed from Kali Linux and correlated in real time. Over <b>12,600+ telemetry events</b> were successfully collected, categorized by custom decoders/rules, and mapped against the MITRE ATT&CK enterprise matrix.", callout_style)]
    ]
    t_abs = Table(abstract_box, colWidths=[504])
    t_abs.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#94A3B8")),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_abs)

    story.append(PageBreak())

    # =========================================================================
    # 2. CHAPTER 1: INTRODUCTION & PROJECT SCOPE
    # =========================================================================
    story.append(Paragraph("1. Introduction, Objectives & Problem Statement", h1_style))
    story.append(Paragraph("In modern enterprise IT environments, security visibility is often severely compromised by fragmented logging mechanisms, high alert fatigue, and lack of host-level process context. Standard operating system event logs (such as generic Windows Security Events or standard Linux syslogs) typically record high-level authentication summaries without providing granular process lineage (Parent Process ID, command-line arguments, process GUIDs, or binary hashes).", body_style))
    story.append(Paragraph("To address these challenges, this project implements a practical, cost-effective Security Operations Center (SOC) environment that unifies:", body_style))
    story.append(Paragraph("• <b>Centralized SIEM Management:</b> Wazuh Manager for log ingestion, decoder parsing, and alert correlation.", bullet_style))
    story.append(Paragraph("• <b>High-Performance Indexing:</b> Wazuh Indexer (OpenSearch) for multi-field search and aggregate analytical dashboards.", bullet_style))
    story.append(Paragraph("• <b>Deep Windows Telemetry:</b> Microsoft Sysmon capturing process creation, network bindings, and registry modifications.", bullet_style))
    story.append(Paragraph("• <b>Kernel-Level Linux Telemetry:</b> Sysmon for Linux (`sysmonforlinux`) leveraging eBPF tracepoints without kernel instability.", bullet_style))
    story.append(Paragraph("• <b>Empirical Threat Validation:</b> Controlled attack simulations from Kali Linux to test and tune detection rules.", bullet_style))

    story.append(Spacer(1, 5))

    # =========================================================================
    # 3. CHAPTER 2: LAB ARCHITECTURE & TOPOLOGY
    # =========================================================================
    story.append(Paragraph("2. Lab Architecture & Network Topology", h1_style))
    story.append(Paragraph("The entire laboratory is virtualized on Oracle VirtualBox using an isolated NAT Network (`10.0.2.0/24`), enabling high-speed communication while isolating traffic from the production home network.", body_style))

    vm_specs = [
        [Paragraph("Host / Node", table_header), Paragraph("Operating System", table_header), Paragraph("IP Address", table_header), Paragraph("Hardware Specs", table_header), Paragraph("Primary Role in Lab", table_header)],
        [Paragraph("<b>Wazuh Server</b>", table_cell_bold), Paragraph("Ubuntu Server 24.04 LTS", table_cell), Paragraph("10.0.2.15", table_cell), Paragraph("4 GB RAM, 2 vCPU, 50 GB", table_cell), Paragraph("SIEM Manager, Indexer & Dashboard", table_cell)],
        [Paragraph("<b>Victim Endpoint</b>", table_cell_bold), Paragraph("Windows 11 Pro (64-bit)", table_cell), Paragraph("10.0.2.20", table_cell), Paragraph("4 GB RAM, 2 vCPU, 60 GB", table_cell), Paragraph("Monitored Endpoint (Agent + Sysmon)", table_cell)],
        [Paragraph("<b>Attacker Node</b>", table_cell_bold), Paragraph("Kali Linux (Rolling)", table_cell), Paragraph("10.0.2.30", table_cell), Paragraph("2 GB RAM, 2 vCPU, 30 GB", table_cell), Paragraph("Offensive Recon & Attack Platform", table_cell)],
        [Paragraph("<b>Host Machine</b>", table_cell_bold), Paragraph("Windows 11 Physical", table_cell), Paragraph("Gateway / Host", table_cell), Paragraph("16 GB RAM, Core i7", table_cell), Paragraph("VirtualBox Hypervisor Host", table_cell)]
    ]
    t_vm = Table(vm_specs, colWidths=[80, 105, 65, 110, 144])
    t_vm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), dark_blue),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [bg_light, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_vm)
    story.append(Spacer(1, 8))

    story.extend(create_image_box("screenshots/02-virtualbox-home.png", "Oracle VirtualBox Environment Hosting Ubuntu Server, Windows 11, and Kali Linux", 500, 200, caption_style))

    story.append(PageBreak())

    # =========================================================================
    # 4. CHAPTER 3: WAZUH SIEM DEPLOYMENT & DASHBOARD VERIFICATION
    # =========================================================================
    story.append(Paragraph("3. Wazuh SIEM Deployment & Dashboard Architecture", h1_style))
    story.append(Paragraph("The Wazuh SIEM platform operates through three tightly coupled subsystems on the Ubuntu 24.04 host:", body_style))
    story.append(Paragraph("1. <b>Wazuh Manager (`wazuh-manager`):</b> Listens on TCP port 1514 for TLS-encrypted agent communication and port 1515 for dynamic agent registration. Decodes incoming logs and matches them against XML correlation rules in real time.", body_style))
    story.append(Paragraph("2. <b>Wazuh Indexer (`wazuh-indexer`):</b> Powered by OpenSearch, it indexes incoming security events into structured document shards (`wazuh-alerts-*` and `wazuh-archives-*`), supporting instant full-text and field-specific filtering.", body_style))
    story.append(Paragraph("3. <b>Wazuh Dashboard (`wazuh-dashboard`):</b> A modern web interface running over HTTPS (TCP port 443) providing Security Events overview, MITRE ATT&CK visualization, Threat Hunting panels, and Regulatory Compliance reports.", body_style))

    story.extend(create_image_box("screenshots/13-wazuh-dashboard-home.png", "Wazuh Dashboard Overview Presenting Real-Time Security Events and System Status", 500, 210, caption_style))

    story.extend(create_image_box("screenshots/19-active-agents.png", "Wazuh Manager Active Multi-Platform Agents Summary (Windows 11 and Kali Linux)", 500, 190, caption_style))

    story.append(PageBreak())

    # =========================================================================
    # 5. CHAPTER 4: ENDPOINT TELEMETRY & SYSMON INTEGRATION
    # =========================================================================
    story.append(Paragraph("4. Endpoint Telemetry & Sysmon Integration (Windows & Linux)", h1_style))
    story.append(Paragraph("Microsoft Sysmon provides high-fidelity endpoint activity monitoring by hooking deep system routines. In this project, Sysmon was deployed on both Windows 11 and Linux to establish unified, cross-platform telemetry.", body_style))

    sysmon_table = [
        [Paragraph("Event ID", table_header), Paragraph("Event Name", table_header), Paragraph("Target OS", table_header), Paragraph("Operational SOC Value & Threat Coverage", table_header)],
        [Paragraph("<b>1</b>", table_cell_bold), Paragraph("Process Creation", table_cell), Paragraph("Win & Linux", table_cell), Paragraph("Captures full CLI arguments, ParentProcessId, ProcessGuid, hashes, user context.", table_cell)],
        [Paragraph("<b>3</b>", table_cell_bold), Paragraph("Network Connect", table_cell), Paragraph("Win & Linux", table_cell), Paragraph("Records source/destination IP, port, initiating binary, and protocol (TCP/UDP).", table_cell)],
        [Paragraph("<b>5</b>", table_cell_bold), Paragraph("Process Terminate", table_cell), Paragraph("Win & Linux", table_cell), Paragraph("Tracks process lifecycle duration and malware termination behaviors.", table_cell)],
        [Paragraph("<b>9</b>", table_cell_bold), Paragraph("Raw Access Read", table_cell), Paragraph("Linux", table_cell), Paragraph("Detects direct device access (`/dev/sda`, memory scraping, credential theft).", table_cell)],
        [Paragraph("<b>11</b>", table_cell_bold), Paragraph("File Create", table_cell), Paragraph("Win & Linux", table_cell), Paragraph("Detects dropper payloads in `/tmp/`, `C:\\Windows\\Temp`, and startup directories.", table_cell)],
        [Paragraph("<b>12/13</b>", table_cell_bold), Paragraph("Registry Event", table_cell), Paragraph("Windows", table_cell), Paragraph("Monitors Run/RunOnce persistence keys and defensive software disablement.", table_cell)],
        [Paragraph("<b>23</b>", table_cell_bold), Paragraph("File Delete", table_cell), Paragraph("Win & Linux", table_cell), Paragraph("Tracks anti-forensic evidence destruction and ransomware file wiping.", table_cell)]
    ]
    t_sys = Table(sysmon_table, colWidths=[45, 95, 65, 299])
    t_sys.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), dark_blue),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [bg_light, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_sys)
    story.append(Spacer(1, 8))

    story.extend(create_image_box("screenshots/21-sysmon-installation.png", "Sysmon Installation on Windows 11 via PowerShell with Schema Validation", 500, 110, caption_style))

    story.extend(create_image_box("screenshots/23-event-viewer-sysmon.png", "Windows Event Viewer Displaying Ingested Sysmon Operational Logs (Event ID 1)", 500, 200, caption_style))

    story.append(PageBreak())

    # =========================================================================
    # 6. CHAPTER 5: CRITICAL COMMAND REFERENCE ACROSS ALL NODES
    # =========================================================================
    story.append(Paragraph("5. Critical Command Reference Across All Lab Nodes", h1_style))
    story.append(Paragraph("To ensure operational efficiency, reproducible administration, and rapid troubleshooting, the most critical commands executed across each lab machine are documented below:", body_style))

    # Ubuntu / Wazuh Manager Commands
    story.append(Paragraph("A. Wazuh Server / Ubuntu Commands (Management, Ingestion & Analysis)", h2_style))
    ubuntu_cmds = [
        [Paragraph("Operation Category", table_header), Paragraph("Command Line Syntax", table_header), Paragraph("Operational Function & Purpose", table_header)],
        [Paragraph("<b>Service Control</b>", table_cell_bold), Paragraph("`sudo systemctl status wazuh-manager wazuh-indexer wazuh-dashboard`", table_cell_code), Paragraph("Verify status of all core SIEM daemons.", table_cell)],
        [Paragraph("<b>Agent Management</b>", table_cell_bold), Paragraph("`sudo /var/ossec/bin/agent_control -l`", table_cell_code), Paragraph("List all registered, active, and disconnected agents.", table_cell)],
        [Paragraph("<b>Agent Info</b>", table_cell_bold), Paragraph("`sudo /var/ossec/bin/agent_control -i 003`", table_cell_code), Paragraph("Query detailed operating telemetry for agent ID 003.", table_cell)],
        [Paragraph("<b>Rule Testing</b>", table_cell_bold), Paragraph("`sudo /var/ossec/bin/wazuh-logtest`", table_cell_code), Paragraph("Interactive log decoder and rule matching simulator.", table_cell)],
        [Paragraph("<b>Live Alerts Stream</b>", table_cell_bold), Paragraph("`sudo tail -f /var/ossec/logs/alerts/alerts.json`", table_cell_code), Paragraph("Stream raw JSON alert output as events trigger.", table_cell)],
        [Paragraph("<b>Firewall Rules</b>", table_cell_bold), Paragraph("`sudo ufw allow 1514/tcp && sudo ufw allow 1515/tcp && sudo ufw allow 443/tcp`", table_cell_code), Paragraph("Open agent log ingestion, registration & web UI ports.", table_cell)],
        [Paragraph("<b>Manager Logs</b>", table_cell_bold), Paragraph("`sudo tail -n 100 /var/ossec/logs/ossec.log`", table_cell_code), Paragraph("Inspect internal manager errors and parsing issues.", table_cell)]
    ]
    t_ub = Table(ubuntu_cmds, colWidths=[100, 240, 164])
    t_ub.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), dark_blue),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [bg_light, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_ub)
    story.append(Spacer(1, 6))

    # Windows 11 Commands
    story.append(Paragraph("B. Windows 11 Endpoint Commands (PowerShell / CMD as Administrator)", h2_style))
    win_cmds = [
        [Paragraph("Operation Category", table_header), Paragraph("Command Line Syntax", table_header), Paragraph("Operational Function & Purpose", table_header)],
        [Paragraph("<b>Sysmon Install</b>", table_cell_bold), Paragraph("`cd C:\\Sysmon; .\\Sysmon64.exe -accepteula -i sysmonconfig.xml`", table_cell_code), Paragraph("Install and activate Sysmon system service with XML config.", table_cell)],
        [Paragraph("<b>Sysmon Config Update</b>", table_cell_bold), Paragraph("`.\\Sysmon64.exe -c sysmonconfig.xml`", table_cell_code), Paragraph("Reload updated Sysmon XML filtering configuration.", table_cell)],
        [Paragraph("<b>Sysmon Service Check</b>", table_cell_bold), Paragraph("`Get-Service Sysmon64`", table_cell_code), Paragraph("Verify Sysmon service status is in 'Running' state.", table_cell)],
        [Paragraph("<b>Wazuh Service Control</b>", table_cell_bold), Paragraph("`NET STOP WazuhSvc; NET START WazuhSvc`", table_cell_code), Paragraph("Restart Windows Wazuh Agent service to reload configuration.", table_cell)],
        [Paragraph("<b>Query Sysmon Logs</b>", table_cell_bold), Paragraph("`Get-WinEvent -LogName 'Microsoft-Windows-Sysmon/Operational' -MaxEvents 5`", table_cell_code), Paragraph("Read recent local Sysmon events directly via PowerShell.", table_cell)],
        [Paragraph("<b>Query Failed Logons</b>", table_cell_bold), Paragraph("`Get-WinEvent -FilterHashtable @{LogName='Security';ID=4625}`", table_cell_code), Paragraph("Inspect Windows Event 4625 failed login entries.", table_cell)],
        [Paragraph("<b>Connectivity Test</b>", table_cell_bold), Paragraph("`Test-NetConnection -ComputerName 10.0.2.15 -Port 1514`", table_cell_code), Paragraph("Test TCP port reachability to the Wazuh Manager.", table_cell)]
    ]
    t_win = Table(win_cmds, colWidths=[105, 235, 164])
    t_win.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), dark_blue),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [bg_light, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_win)
    story.append(Spacer(1, 6))

    # Kali Linux Commands
    story.append(Paragraph("C. Kali Linux Attacker & Linux Telemetry Commands", h2_style))
    kali_cmds = [
        [Paragraph("Attack Phase / Role", table_header), Paragraph("Command Line Syntax", table_header), Paragraph("Offensive & Defensive Objective", table_header)],
        [Paragraph("<b>Host Discovery</b>", table_cell_bold), Paragraph("`nmap -sn 10.0.2.0/24`", table_cell_code), Paragraph("Perform ICMP/ARP ping sweep to discover live subnet hosts.", table_cell)],
        [Paragraph("<b>TCP Port & OS Scan</b>", table_cell_bold), Paragraph("`nmap -sS -sV -O -T4 10.0.2.20`", table_cell_code), Paragraph("SYN stealth scan to enumerate open ports, services, and OS.", table_cell)],
        [Paragraph("<b>Aggressive Scan</b>", table_cell_bold), Paragraph("`nmap -A -p 80,443,3389 10.0.2.20`", table_cell_code), Paragraph("Execute script scans, traceroute, and version detection.", table_cell)],
        [Paragraph("<b>RDP Brute Force</b>", table_cell_bold), Paragraph("`hydra -l administrator -P rockyou.txt rdp://10.0.2.20`", table_cell_code), Paragraph("Simulate high-frequency credential stuffing against Windows.", table_cell)],
        [Paragraph("<b>Sysmon Linux Service</b>", table_cell_bold), Paragraph("`sudo sysmon -accepteula -i /etc/sysmon/sysmonconfig.xml`", table_cell_code), Paragraph("Activate eBPF kernel telemetry collector on Linux.", table_cell)],
        [Paragraph("<b>Sysmon Linux Logs</b>", table_cell_bold), Paragraph("`sudo journalctl -u sysmon -f` or `sudo tail -f /var/log/syslog`", table_cell_code), Paragraph("Stream live Linux Sysmon process and socket events.", table_cell)]
    ]
    t_kali = Table(kali_cmds, colWidths=[105, 235, 164])
    t_kali.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), dark_blue),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [bg_light, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_kali)

    story.append(PageBreak())

    # =========================================================================
    # 7. CHAPTER 6: DETECTION ENGINEERING & RULE ANALYSIS
    # =========================================================================
    story.append(Paragraph("6. Detection Engineering & Custom Rule Authoring", h1_style))
    story.append(Paragraph("Wazuh features a modular rules engine. To detect threats that evade standard signatures, custom rules were developed in `/var/ossec/etc/rules/local_rules.xml`:", body_style))

    story.append(Paragraph("Implemented Custom Detection Rules (`local_rules.xml`)", h2_style))
    
    xml_rules_code = """<group name="custom_rules,sysmon,threat_hunting">
  <!-- Rule 100001: Reconnaissance Port Scanning Detection -->
  <rule id="100001" level="8" frequency="8" timeframe="10">
    <if_matched_group>sysmon_network_connect</if_matched_group>
    <same_source_ip />
    <description>Potential Network Reconnaissance / Rapid Port Scan Detected</description>
    <mitre><id>T1595.001</id></mitre>
  </rule>

  <!-- Rule 100002: Encoded PowerShell & Execution Policy Bypass -->
  <rule id="100002" level="10">
    <if_group>sysmon_process_create</if_group>
    <field name="win.eventdata.commandLine" type="pcre2">(?i)-enc|-encodedcommand|-exec.*bypass</field>
    <description>Suspicious Encoded or Obfuscated PowerShell CLI Execution</description>
    <mitre><id>T1059.001</id></mitre>
  </rule>

  <!-- Rule 100003: Multiple Logon Failures (Brute-Force Threshold) -->
  <rule id="100003" level="12" frequency="5" timeframe="60">
    <if_matched_sid>18152</if_matched_sid>
    <same_source_ip />
    <description>Potential RDP / Windows Authentication Brute-Force in Progress</description>
    <mitre><id>T1110.001</id></mitre>
  </rule>
</group>"""

    story.append(create_code_box(xml_rules_code, code_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("MITRE ATT&CK Matrix Mapping", h2_style))
    mitre_data = [
        [Paragraph("Tactic", table_header), Paragraph("Technique ID", table_header), Paragraph("Technique Name", table_header), Paragraph("Telemetry Source", table_header), Paragraph("Alert Rule Triggered", table_header)],
        [Paragraph("Reconnaissance", table_cell_bold), Paragraph("T1595.001", table_cell), Paragraph("Port Scanning", table_cell), Paragraph("Sysmon Event ID 3", table_cell), Paragraph("Rule 100001 (Rapid Port Scan)", table_cell)],
        [Paragraph("Credential Access", table_cell_bold), Paragraph("T1110.001", table_cell), Paragraph("Password Guessing", table_cell), Paragraph("Event ID 4625", table_cell), Paragraph("Rule 18152 & Rule 100003", table_cell)],
        [Paragraph("Execution", table_cell_bold), Paragraph("T1059.001", table_cell), Paragraph("PowerShell CLI", table_cell), Paragraph("Sysmon Event ID 1", table_cell), Paragraph("Rule 100002 (Encoded CLI)", table_cell)],
        [Paragraph("Persistence", table_cell_bold), Paragraph("T1547.001", table_cell), Paragraph("Registry Run Keys", table_cell), Paragraph("Sysmon Event 12/13", table_cell), Paragraph("Rule 100004 (Registry RunKey)", table_cell)],
        [Paragraph("Defense Evasion", table_cell_bold), Paragraph("T1070.004", table_cell), Paragraph("File Deletion", table_cell), Paragraph("Sysmon Event ID 23", table_cell), Paragraph("Rule 100005 (File Deletion)", table_cell)]
    ]
    t_mitre = Table(mitre_data, colWidths=[80, 75, 105, 110, 134])
    t_mitre.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), dark_blue),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [bg_light, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_mitre)

    story.append(PageBreak())

    # =========================================================================
    # 8. CHAPTER 7: THREAT HUNTING, INGESTION RESULTS & DASHBOARDS
    # =========================================================================
    story.append(Paragraph("7. Threat Hunting, Ingestion Metrics & Analytical Results", h1_style))
    story.append(Paragraph("Over the testing period, the Wazuh SIEM platform ingested and correlated high volumes of telemetry across all endpoints:", body_style))

    metrics_table = [
        [Paragraph("Telemetry Stream", table_header), Paragraph("Source Node", table_header), Paragraph("Total Events Ingested", table_header), Paragraph("Key Ingested Types", table_header), Paragraph("Alert Severity Levels", table_header)],
        [Paragraph("<b>Sysmon for Linux (eBPF)</b>", table_cell_bold), Paragraph("Kali Linux (004)", table_cell), Paragraph("<b>10,135+ Events</b>", table_cell_bold), Paragraph("Process Terminate (5), Process Create (1)", table_cell), Paragraph("Level 3 to Level 10", table_cell)],
        [Paragraph("<b>Windows Sysmon & Events</b>", table_cell_bold), Paragraph("Windows 11 (003)", table_cell), Paragraph("<b>1,427+ Events</b>", table_cell_bold), Paragraph("Process Create (1), Network (3), Event 4625", table_cell), Paragraph("Level 3 to Level 12", table_cell)],
        [Paragraph("<b>Linux PAM & Auth Logs</b>", table_cell_bold), Paragraph("Ubuntu / Kali", table_cell), Paragraph("<b>1,044+ Events</b>", table_cell_bold), Paragraph("Rule 5502 (PAM sudo session), sshd logs", table_cell), Paragraph("Level 3 to Level 8", table_cell)],
        [Paragraph("<b>Total Lab Telemetry</b>", table_cell_bold), Paragraph("All Multi-Nodes", table_cell), Paragraph("<b>12,600+ Events</b>", table_cell_bold), Paragraph("Cross-platform unified log correlation", table_cell), Paragraph("Unified SIEM Ingestion", table_cell)]
    ]
    t_met = Table(metrics_table, colWidths=[110, 85, 95, 124, 90])
    t_met.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), dark_blue),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [bg_light, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_met)
    story.append(Spacer(1, 8))

    story.extend(create_image_box("screenshots/24-sysmon-events-dashboard.png", "Wazuh Discover Ingestion of Over 1,400+ Windows Sysmon Process Events", 500, 200, caption_style))

    story.extend(create_image_box("screenshots/24c-sysmon-linux-events-dashboard.png", "Wazuh Discover Ingestion of 10,135+ Linux Sysmon Events via eBPF Kernel Tracepoints", 500, 200, caption_style))

    story.append(PageBreak())

    # =========================================================================
    # 9. CHAPTER 8: SECURITY ALERT DETAILS & FORENSIC EVIDENCE
    # =========================================================================
    story.append(Paragraph("8. Security Alert Details & Forensic Investigation", h1_style))
    story.append(Paragraph("When attack events trigger threshold conditions, Wazuh generates detailed alert records containing full metadata for forensic analysis:", body_style))

    story.extend(create_image_box("screenshots/19d-dashboard-failed-logon.png", "Wazuh Alert Detail View: Windows Logon Failure (Rule 18152 / Event ID 4625)", 500, 200, caption_style))

    story.extend(create_image_box("screenshots/22-agent-threat-hunting-events.png", "Real-Time Threat Hunting Events Table Showing Rule IDs, Levels, and CIS Benchmarks", 500, 200, caption_style))

    story.append(PageBreak())

    # =========================================================================
    # 10. CHAPTER 9: OPERATIONAL TROUBLESHOOTING & HARDENING
    # =========================================================================
    story.append(Paragraph("9. Operational Troubleshooting & Hardening", h1_style))
    story.append(Paragraph("Throughout the engineering lifecycle of this SOC lab, several operational challenges were diagnosed and resolved:", body_style))

    story.append(Paragraph("• <b>Firewall & Agent Connectivity:</b> Resolved agent connection timeouts by explicitly permitting TCP ports 1514 (log stream) and 1515 (enrollment) in Ubuntu UFW. Tested connectivity using `Test-NetConnection -Port 1514` from Windows.", bullet_style))
    story.append(Paragraph("• <b>Sysmon Event Channel Subscriptions:</b> Resolved missing Sysmon telemetry on Windows by adding the `<location>Microsoft-Windows-Sysmon/Operational</location>` channel with `<log_format>eventchannel</log_format>` inside `ossec.conf`.", bullet_style))
    story.append(Paragraph("• <b>Linux eBPF Kernel Compatibility:</b> Resolved Sysmon for Linux compilation warnings by confirming host Linux kernel version was >= 5.4 with BPF filesystem mounted at `/sys/fs/bpf`.", bullet_style))
    story.append(Paragraph("• <b>Agent Service Daemon Recovery:</b> Created rapid recovery workflows (`NET START WazuhSvc` on Windows and `systemctl restart wazuh-agent` on Linux) to recover from system sleep/hibernation disconnections.", bullet_style))

    story.append(Spacer(1, 8))

    # =========================================================================
    # 11. CHAPTER 10: CONCLUSION & FUTURE ROADMAP
    # =========================================================================
    story.append(Paragraph("10. Conclusion & Future Roadmap", h1_style))
    story.append(Paragraph("This project successfully demonstrated the end-to-end design, implementation, offensive simulation, and defensive monitoring of an enterprise-caliber Security Operations Center (SOC) home laboratory. By uniting Wazuh SIEM with Microsoft Sysmon and eBPF technology, the lab delivers actionable visibility across multi-stage cyber threats.", body_style))

    story.append(Paragraph("Future Enhancements Roadmap", h2_style))
    story.append(Paragraph("• <b>Network Intrusion Detection (NIDS):</b> Integrate Suricata for deep packet inspection and network-level exploit detection.", bullet_style))
    story.append(Paragraph("• <b>Threat Intelligence & Enrichment:</b> Connect VirusTotal, AbuseIPDB, and AlienVault OTX APIs into Wazuh for automated IoC scoring.", bullet_style))
    story.append(Paragraph("• <b>SOAR Automation:</b> Deploy Shuffle SOAR to automate active response actions (such as automated endpoint network isolation upon critical alert triggers).", bullet_style))
    story.append(Paragraph("• <b>Incident Management:</b> Integrate TheHive and MISP for structured security incident ticketing and collaborative threat intel sharing.", bullet_style))

    story.append(Spacer(1, 15))
    story.append(HRFlowable(width="100%", thickness=1, color=border_color, spaceBefore=8, spaceAfter=12))

    signoff = [
        [Paragraph("<b>Project Status:</b> COMPLETED & VERIFIED", body_style), Paragraph("<b>Lead Author:</b> Natto Muni Chakma", body_style)],
        [Paragraph("<b>Degree Program:</b> B.Tech Computer Science & Eng.", body_style), Paragraph("<b>Institution:</b> Andhra University College of Eng.", body_style)],
        [Paragraph("<b>Project Demonstration:</b> https://youtu.be/duEibRGYMHo", body_style), Paragraph("<b>GitHub Repository:</b> github.com/NATTOMR", body_style)]
    ]
    t_sign = Table(signoff, colWidths=[252, 252])
    t_sign.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_sign)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Professional Report successfully generated: {filename}")

if __name__ == "__main__":
    build_pdf()

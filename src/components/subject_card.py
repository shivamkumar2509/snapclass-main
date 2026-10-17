
import streamlit as st
import html


def subject_card(name, code, section, stats=None, footer_callback=None):
    name = html.escape(str(name))
    code = html.escape(str(code))
    section = html.escape(str(section))

    stats_html = ""

    if stats:
        items = []

        for icon, label, value in stats:
            items.append(f"""
                <div style="
                    background: #FCE7F3;
                    padding: 8px 14px;
                    border-radius: 12px;
                    font-size: 14px;
                    color: #374151;
                ">
                    {icon}
                    <b>{html.escape(str(value))}</b>
                    {html.escape(str(label))}
                </div>
            """)

        stats_html = f"""
            <div style="
                display: flex;
                gap: 10px;
                flex-wrap: wrap;
                margin-top: 18px;
            ">
                {''.join(items)}
            </div>
        """

    card_html = f"""
        <div style="
            background: #FFFFFF;
            padding: 24px;
            border-radius: 16px;
            border: 1px solid #E5E7EB;
            border-left: 7px solid #EB459E;
            margin-bottom: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            color: #1E293B;
        ">
            <h3 style="
                margin: 0;
                color: #1E293B;
                font-size: 24px;
            ">
                {name}
            </h3>

            <p style="
                color: #64748B;
                margin: 12px 0 0 0;
                font-size: 14px;
            ">
                Code:
                <span style="
                    background: #E0E3FF;
                    color: #5865F2;
                    padding: 4px 9px;
                    border-radius: 6px;
                ">{code}</span>

                &nbsp; | &nbsp; Section:

                <span style="
                    background: #FCE7F3;
                    color: #BE459E;
                    padding: 4px 9px;
                    border-radius: 6px;
                ">{section}</span>
            </p>

            {stats_html}
        </div>
    """

    st.html(card_html)

    if footer_callback:
        footer_callback()

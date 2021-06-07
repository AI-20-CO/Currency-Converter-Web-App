from forex_python.converter import CurrencyCodes
from forex_python.bitcoin import BtcConverter
import streamlit as st
from google_currency import convert

# Page layout
st.set_page_config(page_title=' Currency Converter', page_icon='💱',initial_sidebar_state='collapsed')

# Putting the whole program in try except so no errors could be displayed on the main page
try:
    # getting the codes before hand so it doesn't take more run time
    curr = CurrencyCodes()
    # Side bar layout
    st.sidebar.header('| NAVIGATE 🔘 |')
    selection = st.sidebar.selectbox('', ['💰 Currency converter 💱', 'About 📜'])

    if selection == 'About 📜':
        # simple html code to make the page vibrant
        about_info1 = '''<div
         style="background-image: linear-gradient(to right, #f63366, #fffd80);padding:2px;border-radius:9px">
         </div> '''
        st.markdown(about_info1, unsafe_allow_html=True)

        # writing the text using html
        st.text('')
        about_info2 = '''<div
         style="background-color:rgb(14, 17, 23);padding:2px;border-radius:9px">
         <h2 
         style="color:white;text-align:center;font-size:20px">DEVELOPER : AYAAN IZHAR
         </h2> 
         </div> '''
        st.markdown(about_info2, unsafe_allow_html=True)
        st.text('')

        # simple html code to make the page vibrant
        about_info3 = '''<div
         style="background-image: linear-gradient(to left, #f63366, #fffd80);padding:2px;border-radius:9px">
         </div> '''
        st.markdown(about_info3, unsafe_allow_html=True)
        st.text('')

        # git hub link in the form of button
        st.header(
            'Link - ' + '[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github)](https://github.com/Ayaan-20)')

        # Creating a button
        more_about = st.button('● More to know ● ')
        if more_about:
            more = '''<div
             style="background-color: rgb(14, 17, 23);padding:10px;border-radius:20px"> 
             <h2 
             style="color:white;text-align:start;font-size:20px">I am a high school python programmer and this is a Currency Converter  💱
             web app which converts currency from 60 different countries. I hope you like it !
             </h2> 
             </div> '''
            st.markdown(more, unsafe_allow_html=True)

    # The main web app
    elif selection == '💰 Currency converter 💱':
        
        # Making 3 columns
        num11, input_from1, input_to1 = st.beta_columns(3)

        # Asking user to enter the amount
        num1 = float(num11.text_input('Amount 💵 : ', value=1))

        # Setting a limit on how many numbers can the user enter to convert
        if len(str(num1)) > 18:
            st.info(': The number entered is too large : ')
        else:
            # Set of the countries whose currency can be converted
            # Making a from selection
            input_from = input_from1.selectbox('Country from 🌍 : ',
                                               ['', 'usd ( united states )', 'cad ( canada )', 'aed ( dubai )', 'afn (afghanistan)',
                                                'inr ( india )',
                                                'sar ( saudi arabia ) ',
                                                'eur ( austria ) ', 'aud ( australia )', 'ars ( argentina )', 'gbp ( pound sterling )',
                                                'nzd ( new zealand )', 'amd ( armenia )', 'azn ( azerbaijan )', 'dkk ( denmark )',
                                                'bhd ( bahrain )', 'bdt ( bangladesh )', 'cny ( china )', 'cnh ( chinese )',
                                                'cop ( colombia )', 'clf ( chile )',
                                                'egp ( egypt )', 'kgs ( kyrgyzstan )',
                                                'gel ( georgia )', 'hkd ( hong kong )', 'huf ( hungary )', 'isk ( iceland )',
                                                'idr ( indonesia )', 'irr ( iran )', 'xcd ( grenada )',
                                                'iqd ( iraq )', 'ils ( israel )', 'jmd ( jamaica )', 'jpy ( japan )', 'jod ( jordan )',
                                                'kzt ( kazakhstan )', 'kes ( kenya )', 'kwd ( kuwait )',
                                                'lbp ( lebanon )', 'lyd ( libya )', 'myr ( malaysia )', 'mxn ( mexico )',
                                                'npr ( nepal )', 'omr ( oman )', 'pkr ( pakistan )', 'php ( philippines )',
                                                'pln ( poland )', 'lrd ( liberia )', 'mvr ( maldives )',
                                                'qar ( qatar )', 'sgd ( singapore)', 'lkr ( sri lanka )',
                                                'sek ( sweden )', 'chf ( switzerland )', 'tjs ( tajikistan )', 'thb ( thailand )',
                                                'try ( turkey )', 'ugx ( uganda )', 'yer ( yemen )', 'mad ( western sahara )'])

            # Making a to selection
            input_to = input_from1.selectbox('Country to 🗺️ : ',
                                               ['', 'usd ( united states )', 'cad ( canada )', 'aed ( dubai )', 'afn (afghanistan)',
                                                'inr ( india )',
                                                'sar ( saudi arabia ) ',
                                                'eur ( austria ) ', 'aud ( australia )', 'ars ( argentina )', 'gbp ( pound sterling )',
                                                'nzd ( new zealand )', 'amd ( armenia )', 'azn ( azerbaijan )', 'dkk ( denmark )',
                                                'bhd ( bahrain )', 'bdt ( bangladesh )', 'cny ( china )', 'cnh ( chinese )',
                                                'cop ( colombia )', 'clf ( chile )',
                                                'egp ( egypt )', 'kgs ( kyrgyzstan )',
                                                'gel ( georgia )', 'hkd ( hong kong )', 'huf ( hungary )', 'isk ( iceland )',
                                                'idr ( indonesia )', 'irr ( iran )', 'xcd ( grenada )',
                                                'iqd ( iraq )', 'ils ( israel )', 'jmd ( jamaica )', 'jpy ( japan )', 'jod ( jordan )',
                                                'kzt ( kazakhstan )', 'kes ( kenya )', 'kwd ( kuwait )',
                                                'lbp ( lebanon )', 'lyd ( libya )', 'myr ( malaysia )', 'mxn ( mexico )',
                                                'npr ( nepal )', 'omr ( oman )', 'pkr ( pakistan )', 'php ( philippines )',
                                                'pln ( poland )', 'lrd ( liberia )', 'mvr ( maldives )',
                                                'qar ( qatar )', 'sgd ( singapore)', 'lkr ( sri lanka )',
                                                'sek ( sweden )', 'chf ( switzerland )', 'tjs ( tajikistan )', 'thb ( thailand )',
                                                'try ( turkey )', 'ugx ( uganda )', 'yer ( yemen )', 'mad ( western sahara )'])

            # The output comes in a string , so making it proper by using string slice and a for loop
            currency_cnt = convert(input_from[0:3], input_to[0:3], num1)

            # Getting the symbol of the entered currency
            symbol = curr.get_symbol(input_to[0:3].upper())
            
            list1 = []
            length = currency_cnt[40:100]
            for i in currency_cnt:
                if i.isdigit():
                    list1.append(i)

            # Both selection same
            if input_from == input_to:
                num11.markdown('  1.00')

            # Selection different
            else:
                # Double checking if the output of v is a digit
                if currency_cnt[40].isdigit():

                    # Symbol for currency converter
                    num11.markdown('💱')

                    # Output of the converted currency
                    num11.markdown('' + currency_cnt[40:40 + 1 + len(list1)] + ' ' + symbol)

                    # Making a bitcoin converter button
                    button_bit_coin = st.button('Bit coins 💱')
                    if button_bit_coin:
                        # Bit coin converter
                        bt1, bt2 = st.beta_columns(2)
                        bt = BtcConverter()
                        bt1.text(
                            '1' + ' bitcoin' + ' = ' + ' ' + str(bt.get_latest_price(input_to[0:3].upper())) + ' ' + symbol)
                        bt1.text('1' + ' bitcoin' + ' = ' + ' ' + str(
                            bt.get_latest_price(input_from[0:3].upper())) + ' ' + input_from[0:3])

                # If v is not a digit then show nothing
                else:
                    pass

        # Making the layout for a vibrant page
        about_info2 = '''<div
        style="background-image: linear-gradient(to left, #bdc3c7, #2c3e50);padding:2px;border-radius:9px">
        </div> '''
        st.markdown(about_info2, unsafe_allow_html=True)

        # The codes for the user to refer
        st.markdown('''###  
        CODES :
        usd (united states)    bdt (bangladesh)     kes (kenya)        qar (qatar)
        afn (afghanistan)      cny (china)          kwd (kuwait)       sgd (singapore)
        inr (india)            cop (colombia)       lbp (lebanon)      lkr (sri lanka)
        sar (saudi arabia)     hkd (hong kong)      lyd (libya)        sek (sweden)
        eur (austria)          huf (hungary)        myr (malaysia)     chf (switzerland)
        aud (australia)        isk (iceland)        mxn (mexico)       tjs (tajikistan)
        amd (armenia)          iqd (iraq)           npr (nepal)        thb (thailand)
        azn (azerbaijan)       ils (israel)         omr (oman)         try (turkey)
        bhd (bahrain)          jmd (jamaica)        pkr (pakistan)     ugx (uganda)
        egp (egypt)            jpy (japan)          php (philippines)  yer (yemen)
        gel (georgia)          jod (jordan)         pln (poland)       mad (western sahara)
        idr (indonesia)        kzt (kazakhstan)     qar (qatar)        cad (canada)
        gbp (pound sterling)   aed (dubai)          dkk (denmark)      kgs (kyrgyzstan)
        cnh (chinese)          ars (argentina)      xcd (grenada)      lrd (liberia)
        nzd (new zealand)      clf (chile)          irr (iran)         mvr (maldives)
            ''')

except:
    pass

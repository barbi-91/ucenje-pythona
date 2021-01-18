from textwrap import dedent

class Kraj():

    def enter(self):
        print(dedent("""
        ************************************************************************
        ****************************** * *  <3 * <3 * <3  * * ******************
        ************************************************************************
        Pobjedili ste zimu, Bravo!
        * * *  <3 * <3 * <3  * * *
        Ako podijelimo barem malu iskricu topline s onima koje sretnemo na putu,
        zima će postati mnogo toplija, za sve!
        ************************************************************************
        ******************************* * *  <3 * <3 * <3  * * *****************

        """))

        return 'kraj'

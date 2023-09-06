import streamlit as st
from barfi import st_barfi, Block


def main():
  st.header('Node Based Notion Editor', divider='rainbow')

  page = Block(name='Page')
  page.add_input(name='parent')
  page.add_output(name='child')

  db = Block(name='DB')
  db.add_input(name='parent')

  st_barfi(base_blocks=[page, db])


if __name__ == '__main__':
  main()
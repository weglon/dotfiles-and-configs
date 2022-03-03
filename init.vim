set path+=**
set modelines=0
set autoread
au FocusGained,BufEnter * :silent! !
set encoding=utf-8
set visualbell
set backspace=indent,eol,start
set nobackup
set noswapfile
set mouse=a
set number
set scrolloff=2
set expandtab tabstop=2 shiftwidth=2 softtabstop=2
set autoindent
set showmode showcmd
set lazyredraw
set showmatch
set hlsearch incsearch ignorecase smartcase
set autochdir
set hidden
set wildmenu wildmode=list:longest,full
set laststatus=2 statusline=%F
set clipboard=unnamedplus
set foldmethod=indent
set foldnestmax=1
set foldlevelstart=1
set termguicolors
set noshowmode

"General navigation  
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-h> <C-w>h
nnoremap <C-l> <C-w>l
"Editor stuff
nnoremap <C-s> :w<CR> :call CocAction('runCommand', 'prettier.formatFile')<CR>
inoremap <C-s> <Esc>:w<CR>:call CocAction('runCommand', 'prettier.formatFile')<CR>a
nnoremap <C-z> u
inoremap <C-z> <Esc>u i<Up>
nnoremap <C-z> u
nnoremap <C-e> :q<CR>
nnoremap <Esc> a
nnoremap <Tab> :NERDTreeToggle<CR>
inoremap <C-f> <Esc>/
nnoremap q ciw <Esc>
nnoremap qd ciW <Esc>

"Terminal stuff
nnoremap ä :vsplit<CR>
nnoremap å :split<CR>
nnoremap <C-t> :split<CR> <C-w>j :res -13<CR> :terminal<CR> i
nnoremap t <C-w>j i
tnoremap <Esc> <C-\><C-n><C-w>k

"Bracket and qoute pairing
inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap {;<CR> {<CR>};<ESC>O

call plug#begin('~/.local/share/nvim/plugged')
  " Basic utilities
  Plug 'neoclide/coc.nvim', {'branch': 'release'}
  Plug 'preservim/nerdtree'
  Plug 'honza/vim-snippets'
  Plug 'SirVer/ultisnips'
  Plug 'ryanoasis/vim-devicons'
  Plug 'itchyny/lightline.vim'
  Plug 'ap/vim-css-color'  
  Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}

  " Themes 'n stuff
  Plug 'sjl/badwolf'
  Plug 'junegunn/seoul256.vim'
  Plug 'NLKNguyen/papercolor-theme'
  Plug 'savq/melange'
  Plug 'joshdick/onedark.vim'
  Plug 'ayu-theme/ayu-vim'
  Plug 'morhetz/gruvbox'
  Plug 'lifepillar/vim-gruvbox8'
  Plug 'sainnhe/gruvbox-material'
  Plug 'sainnhe/sonokai'
call plug#end()

" `'default'`, `'atlantis'`, `'andromeda'`, `'shusia'`, `'maia'`, `'espresso'`
" let g:sonokai_cursor = 'orange'
" let g:sonokai_style = 'espresso'
" let g:sonokai_transparent_background = 1

"let g:gruvbox_material_enable_italic = 1
"let g:gruvbox_material_enable_bold = 1
"let g:gruvbox_material_background = 'soft'
"let g:gruvbox_material_statusline_style = 'original'
"let g:gruvbox_material_diagnostic_line_highlight = 1
"let g:gruvbox_material_palette = 'mix'

let g:seoul256_background = 236
let g:seoul256_srgb = 1

let g:lightline = {
     \ 'colorscheme': 'sonokai',
     \ 'active': {
     \   'left': [ ['mode', 'paste'],
     \             ['fugitive', 'readonly', 'filename', 'modified'] ],
     \   'right': [ [ 'lineinfo' ], ['percent'] ]
     \ },
     \ 'component': {
     \   'readonly': '%{&filetype=="help"?"":&readonly?"\ue0a2":""}',
     \   'modified': '%{&filetype=="help"?"":&modified?"\ue0a0":&modifiable?"":"-"}',
     \   'fugitive': '%{exists("*fugitive#head")?fugitive#head():""}'
     \ },
     \ 'component_visible_condition': {
     \   'readonly': '(&filetype!="help"&& &readonly)',
     \   'modified': '(&filetype!="help"&&(&modified||!&modifiable))',
     \   'fugitive': '(exists("*fugitive#head") && ""!=fugitive#head())'
     \ },
     \ 'separator': { 'left': "\ue0b4", 'right': "\ue0b6" },
     \ 'subseparator': { 'left': "\ue0b5", 'right': "\ue0b7" },
     \ }

" let g:lightline = {
" \ 'separator': { 'left': "\ue0b4", 'right': "\ue0b6" },
"   \ 'subseparator': { 'left': "\ue0b5", 'right': "\ue0b7" },
"     \ 'colorscheme': 'sonokai'
"     \ }


set foldmethod=expr
set foldexpr=nvim_treesitter#foldexpr()

lua <<EOF
require'nvim-treesitter.configs'.setup {
  -- ensure_installed = "maintained", -- one of "all", "maintained" (parsers with maintainers), or a list of languages
  highlight = {
    enable = true,              -- false will disable the whole extension
    -- disable = { "c", "rust" },  -- list of language that will be disabled
  },
}
EOF

colorscheme gruvbox
hi Normal guibg=NONE ctermbg=NONE
hi EndOfBuffer guibg=NONE ctermbg=NONE

command! -nargs=0 Prettier :call CocAction('runCommand', 'prettier.formatFile')

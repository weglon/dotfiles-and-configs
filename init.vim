set path+=**
set modelines=0
set autoread
au FocusGained,BufEnter * :silent! !
set encoding=UTF-8
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
set nocompatible 
set hidden
set wildmenu wildmode=list:longest,full
set laststatus=2 statusline=%F
set clipboard=unnamedplus
set foldmethod=indent
set foldnestmax=1
set foldlevelstart=1
set termguicolors
set noshowmode
set conceallevel=1

"Navigation  
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-h> <C-w>h
nnoremap <C-l> <C-w>l

"Resizing
nnoremap <A-h> :vertical resize -5<CR> 
nnoremap <A-l> :vertical resize +5<CR> 
nnoremap <A-j> :resize +5<CR> 
nnoremap <A-k> :resize -5<CR> 

"Other editor stuff
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
inoremap ` ``<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap {;<CR> {<CR>};<ESC>O

call plug#begin('~/.local/share/nvim/plugged')
  " Essentials
  Plug 'neoclide/coc.nvim', {'branch': 'release'}
  Plug 'scrooloose/nerdtree'  
  Plug 'honza/vim-snippets'
  Plug 'SirVer/ultisnips'
  Plug 'itchyny/lightline.vim'

  " Syntax highlighting
  " Treesitter for gruvbox, alduin
  " Polygot for everforest, sonokai
  " Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
  " Plug 'sheerun/vim-polyglot'
  " Plug 'tree-sitter/tree-sitter-javascript'
  Plug 'pangloss/vim-javascript'
  Plug 'numirias/semshi', { 'do': ':UpdateRemotePlugins' }

  " Themes
  Plug 'sjl/badwolf'
  Plug 'junegunn/seoul256.vim'
  Plug 'shinchu/lightline-gruvbox.vim'
  Plug 'savq/melange'
  Plug 'joshdick/onedark.vim'
  Plug 'morhetz/gruvbox'
  Plug 'sainnhe/gruvbox-material'
  Plug 'sainnhe/sonokai'
  Plug 'tomasr/molokai'
  Plug 'AlessandroYorba/Alduin'
  Plug 'romainl/Apprentice'
  Plug 'xadillax/vim-mir2-colorscheme'
  Plug 'straw/vim-strawimodo'
  Plug 'scottymoon/vim-twilight'
  Plug 'ahmedabdulrahman/aylin.vim'
  Plug 'sainnhe/everforest'

  " icons
  Plug 'ryanoasis/vim-devicons'
  Plug 'tiagofumo/vim-nerdtree-syntax-highlight'

call plug#end()

let g:lightline = {
    \ 'colorscheme': 'gruvbox', 
    \ 'active': {
    \   'left': [ [ 'mode', 'paste' ],
    \             [ 'gitbranch', 'filename', 'modified' ] ],
    \   'right': [['lineinfo'], ['percent']] 
    \ },
    \ 'component_function': {
    \   'mode': 'LightlineMode',
    \ },
    \ 'separator': { 'left': '', 'right': ''}
    \ }


function! LightlineMode()
  return expand('%:t') =~# '^__Tagbar__' ? 'Tagbar':
    \ expand('%:t') ==# 'ControlP' ? 'CtrlP' :
    \ &filetype ==# 'javascript' ? '' :
    \ &filetype ==# 'json' ? '' :
    \ &filetype ==# 'python' ? '' :
    \ &filetype ==# 'css' ? '' :
    \ &filetype ==# 'vim' ? '' :
    \ &filetype ==# 'html' ? '' :
    \ &filetype ==# 'lua' ? '' : 
    \ &filetype ==# 'typescript' ? '' : 
    \ &filetype ==# 'java' ? '' : 
    \ &filetype ==# 'cpp' ? 'ﭱ' : 
    \ &filetype ==# 'c' ? '' : 
    \ ''
endfunction

let s:brown = "6e4c30"
let s:aqua =  "8ec07c"
let s:blue = "83a598"
let s:darkBlue = "458588"
let s:purple = "d3869b"
let s:lightPurple = "458588"
let s:red = "af3a03"
let s:beige = "a89984"
let s:yellow = "d79921"
let s:darkOrange = "d65d0e"
let s:orange = "fe8019"
let s:pink = "db76a4"
let s:salmon = "db8e76"
let s:green = "98971a"
let s:lightGreen = "98971a"
let s:white = "f9f5d7"
let s:rspec_red = 'fb4934'
let s:git_orange = 'fe8019'

" let g:NERDTreeExtensionHighlightColor = {}
" let g:NERDTreeExtensionHighlightColor['css'] = s:blue
" let g:NERDTreeExtensionHighlightColor['cpp'] = s:blue
" let g:NERDTreeExtensionHighlightColor['c'] = s:blue
" let g:NERDTreeExtensionHighlightColor['h'] = s:blue
" let g:NERDTreeExtensionHighlightColor['js'] = s:yellow
" let g:NERDTreeExtensionHighlightColor['ts'] = s:yellow
" let g:NERDTreeExtensionHighlightColor['json'] = s:pink
" let g:NERDTreeExtensionHighlightColor['node_modules'] = s:pink
" let g:NERDTreeExtensionHighlightColor['html'] = s:darkOrange
" let g:NERDTreeExtensionHighlightColor['xml'] = s:darkBlue
" let g:NERDTreeExtensionHighlightColor['txt'] = s:beige
" let g:NERDTreeExtensionHighlightColor['yml'] = s:darkBlue
" let g:NERDTreeExtensionHighlightColor['java'] = s:red
" let g:NERDTreeExtensionHighlightColor['class'] = s:red
" let g:NERDTreeExtensionHighlightColor['jar'] = s:red
" let g:NERDTreeExtensionHighlightColor['kt'] = s:purple
" let g:NERDTreeExtensionHighlightColor['sh'] = s:green
" let g:NERDTreeExtensionHighlightColor['git'] = s:git_orange
" let g:NERDTreeExtensionHighlightColor['png'] = s:beige
" let g:NERDTreeExtensionHighlightColor['jpg'] = s:beige
" let g:NERDTreeExtensionHighlightColor['.gitignore'] = s:git_orange

let g:NERDTreeFileExtensionHighlightFullName = 1
let g:NERDTreeExactMatchHighlightFullName = 1
let g:NERDTreePatternMatchHighlightFullName = 1

" set foldmethod=expr
" set foldexpr=nvim_treesitter#foldexpr()

" Syntax highlighting pt2
" lua <<EOF
"   require'nvim-treesitter.configs'.setup {
"     ensure_installed = "all",
"     sync_install = false,
"
"     highlight = {
"       enable = true,
"       additional_vim_regex_highlighting = false,
"     },
"   }
" EOF
" let g:polyglot_disabled = ['python']

let g:semshi#always_update_all_highlights = v:true
let g:javascript_conceal_function = "ƒ"
let g:javascript_conceal_this = "@"

colorscheme gruvbox-material

hi Normal guibg=NONE ctermbg=NONE
hi EndOfBuffer guibg=NONE ctermbg=NONE

command! -nargs=0 Prettier :call CocAction('runCommand', 'prettier.formatFile')
